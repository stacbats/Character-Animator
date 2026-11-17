"""
C64 Tile Animator - A GUI tool for creating and animating C64 tiles
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageDraw, ImageTk
import json
import os
from pathlib import Path

# C64 Standard Color Palette
C64_COLORS = {
    "Black": "#000000",
    "White": "#FFFFFF",
    "Red": "#68372B",
    "Cyan": "#70A4B2",
    "Purple": "#6F3D86",
    "Green": "#588D43",
    "Blue": "#352879",
    "Yellow": "#B8C76F",
    "Orange": "#6F4F25",
    "Brown": "#9A6759",
    "Light Red": "#B41E6E",
    "Dark Gray": "#505050",
    "Gray": "#787878",
    "Light Green": "#94E089",
    "Light Blue": "#6C5EB5",
    "Light Gray": "#A6A6A6",
}

class C64TileAnimator:
    def __init__(self, root):
        self.root = root
        self.root.title("C64 Tile Animator")
        self.root.geometry("1200x850")
        
        # State variables
        self.tile_size = tk.IntVar(value=8)
        self.current_color = tk.StringVar(value="White")
        self.zoom_level = tk.IntVar(value=16)
        self.animation_speed = tk.IntVar(value=100)
        self.color_mode = tk.StringVar(value="MULTI-COLOR")
        self.is_animating = False
        
        # Color mode settings
        self.hi_res_colors = ["Black", "White"]  # Background + 1 color
        self.multi_color_colors = ["Black", "White", "Red", "Cyan"]  # Background + 3 colors
        self.selected_colors = {}  # {mode: [colors]}
        self.selected_colors["HI-RES"] = ["Black", "White"]
        self.selected_colors["MULTI-COLOR"] = ["Black", "White", "Red", "Cyan"]
        
        # Tile storage
        self.tiles = []  # List of tile data (each is a dict with pixels)
        self.current_tile_index = 0
        self.pixel_data = {}  # {tile_index: {(x,y): color}}
        
        # Onion skin mode
        self.onion_skin_enabled = tk.BooleanVar(value=False)
        self.onion_skin_tile_index = tk.IntVar(value=-1)  # -1 = previous, or specific tile index
        
        # Create UI
        self.create_ui()
        self.create_new_tile()
        
    def create_ui(self):
        """Create the main UI layout - 3 columns: Editor, Preview, Palette"""
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Top control panel - Grid layout for compact controls
        top_frame = ttk.Frame(main_frame)
        top_frame.pack(fill=tk.X, pady=5)
        
        # Row 1: Tile Size and Color Mode side by side
        size_mode_frame = ttk.Frame(top_frame)
        size_mode_frame.pack(fill=tk.X, pady=5)
        
        # Tile Size
        ttk.Label(size_mode_frame, text="Tile Size", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=(0, 10))
        size_frame = ttk.Frame(size_mode_frame)
        size_frame.pack(side=tk.LEFT, padx=(0, 20))
        for size in [8, 16, 32]:
            ttk.Radiobutton(size_frame, text=f"{size}x{size}", variable=self.tile_size, 
                           value=size, command=self.on_tile_size_changed).pack(side=tk.LEFT, padx=2)
        
        # Color Mode
        ttk.Label(size_mode_frame, text="Color Mode", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=(0, 10))
        mode_frame = ttk.Frame(size_mode_frame)
        mode_frame.pack(side=tk.LEFT, padx=(0, 20))
        ttk.Radiobutton(mode_frame, text="HI-RES (2)", variable=self.color_mode,
                       value="HI-RES", command=self.on_color_mode_changed).pack(side=tk.LEFT, padx=2)
        ttk.Radiobutton(mode_frame, text="MULTI (4)", variable=self.color_mode,
                       value="MULTI-COLOR", command=self.on_color_mode_changed).pack(side=tk.LEFT, padx=2)
        
        # Zoom Level
        ttk.Label(size_mode_frame, text="Zoom", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Scale(size_mode_frame, from_=4, to=32, variable=self.zoom_level, orient=tk.HORIZONTAL,
                 command=lambda v: self.refresh_editor(), length=100).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Label(size_mode_frame, textvariable=self.zoom_level, width=3).pack(side=tk.LEFT)
        
        # Row 2: Color Scheme and Palette side by side
        color_frame = ttk.Frame(top_frame)
        color_frame.pack(fill=tk.X, pady=5)
        
        # Color Scheme Editor
        ttk.Label(color_frame, text="Colors", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=(0, 10))
        self.scheme_frame = ttk.LabelFrame(color_frame, text="Scheme", padding=3)
        self.scheme_frame.pack(side=tk.LEFT, padx=(0, 20))
        
        self.color_selectors = {}
        self.color_buttons = {}
        self.update_color_scheme_ui(self.scheme_frame)
        
        # Selected Color Display
        ttk.Label(color_frame, text="Selected", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=(0, 10))
        self.color_display = tk.Canvas(color_frame, width=40, height=25, bg="white", relief=tk.SUNKEN)
        self.color_display.pack(side=tk.LEFT, padx=(0, 20))
        self.update_color_display()
        
        # Animation Speed
        ttk.Label(color_frame, text="Speed (ms)", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Scale(color_frame, from_=10, to=500, variable=self.animation_speed, orient=tk.HORIZONTAL,
                 length=100).pack(side=tk.LEFT, padx=(0, 5))
        
        # Spacer to push buttons right
        ttk.Frame(color_frame).pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Animation and File buttons
        self.animate_btn = ttk.Button(color_frame, text="Play", command=self.toggle_animation, width=8)
        self.animate_btn.pack(side=tk.LEFT, padx=2)
        ttk.Button(color_frame, text="Save", command=self.save_project, width=8).pack(side=tk.LEFT, padx=2)
        ttk.Button(color_frame, text="Load", command=self.load_project, width=8).pack(side=tk.LEFT, padx=2)
        
        # Main content area - 3 columns: Editor | Preview | Palette
        content_frame = ttk.Frame(main_frame)
        content_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # LEFT COLUMN: Editor + Tile Management + Tile List
        left_content = ttk.Frame(content_frame)
        left_content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        ttk.Label(left_content, text="Tile Editor", font=("Arial", 10, "bold")).pack(anchor=tk.W, pady=2)
        self.editor_canvas = tk.Canvas(left_content, bg="gray30", cursor="crosshair", height=250)
        self.editor_canvas.pack(fill=tk.BOTH, expand=True, pady=2)
        self.editor_canvas.bind("<Button-1>", self.on_canvas_click)
        self.editor_canvas.bind("<B1-Motion>", self.on_canvas_drag)
        self.editor_canvas.bind("<Button-3>", self.on_canvas_right_click)
        
        # Tile Management
        tile_mgmt_frame = ttk.Frame(left_content)
        tile_mgmt_frame.pack(fill=tk.X, pady=2)
        ttk.Button(tile_mgmt_frame, text="New", command=self.create_new_tile, width=8).pack(side=tk.LEFT, padx=2)
        ttk.Button(tile_mgmt_frame, text="Copy", command=self.copy_tile, width=8).pack(side=tk.LEFT, padx=2)
        ttk.Button(tile_mgmt_frame, text="Delete", command=self.delete_tile, width=8).pack(side=tk.LEFT, padx=2)
        ttk.Button(tile_mgmt_frame, text="Clear", command=self.clear_tile, width=8).pack(side=tk.LEFT, padx=2)
        
        # Onion Skin Controls
        onion_frame = ttk.LabelFrame(left_content, text="Onion Skin", padding=3)
        onion_frame.pack(fill=tk.X, pady=(5, 2))
        
        ttk.Checkbutton(onion_frame, text="Enable", variable=self.onion_skin_enabled,
                       command=self.refresh_editor).pack(side=tk.LEFT, padx=2)
        
        ttk.Label(onion_frame, text="Show:").pack(side=tk.LEFT, padx=(5, 2))
        onion_combo = ttk.Combobox(onion_frame, values=["Previous Tile", "Tile 1", "Tile 2", "Tile 3"],
                                   state="readonly", width=12)
        onion_combo.set("Previous Tile")
        onion_combo.pack(side=tk.LEFT, padx=2)
        onion_combo.bind("<<ComboboxSelected>>", self.on_onion_skin_changed)
        
        # Tile List
        ttk.Label(left_content, text="Tiles", font=("Arial", 10, "bold")).pack(anchor=tk.W, pady=(5, 2))
        self.tile_listbox = tk.Listbox(left_content, height=4)
        self.tile_listbox.pack(fill=tk.BOTH, expand=True, pady=2)
        self.tile_listbox.bind('<<ListboxSelect>>', self.on_tile_selected)
        
        # MIDDLE COLUMN: Preview + Stats
        middle_content = ttk.Frame(content_frame)
        middle_content.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0, 5))
        
        ttk.Label(middle_content, text="Preview", font=("Arial", 10, "bold")).pack(anchor=tk.W, pady=2)
        self.preview_canvas = tk.Canvas(middle_content, width=300, height=300, bg="black")
        self.preview_canvas.pack(pady=2)
        
        self.stats_label = ttk.Label(middle_content, text="", justify=tk.LEFT, font=("Courier", 9))
        self.stats_label.pack(anchor=tk.NW, pady=5)
        
        # RIGHT COLUMN: Full Palette (scrollable)
        right_content = ttk.Frame(content_frame, width=150)
        right_content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False, padx=(5, 0))
        right_content.pack_propagate(False)
        
        ttk.Label(right_content, text="Palette", font=("Arial", 10, "bold")).pack(anchor=tk.W, pady=2)
        palette_frame = ttk.Frame(right_content)
        palette_frame.pack(fill=tk.BOTH, expand=True, pady=2)
        
        # Scrollable color list with FULL HEIGHT
        canvas = tk.Canvas(palette_frame, bg="gray20")
        scrollbar = ttk.Scrollbar(palette_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas, style="TFrame")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        for color_name, color_hex in C64_COLORS.items():
            self.create_color_button(scrollable_frame, color_name, color_hex)
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
    def create_color_button(self, parent, name, hex_color):
        """Create a color palette button"""
        btn = tk.Canvas(parent, width=150, height=25, bg=hex_color, relief=tk.RAISED, bd=1)
        btn.pack(fill=tk.X, pady=1)
        btn.bind("<Button-1>", lambda e: self.select_color(name))
        btn.create_text(75, 12, text=name, font=("Arial", 9), fill="white" if self.is_dark(hex_color) else "black")
        
    def is_dark(self, hex_color):
        """Determine if a color is dark"""
        r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)
        return (r * 0.299 + g * 0.587 + b * 0.114) < 128
        
    def select_color(self, color_name):
        """Select a color"""
        self.current_color.set(color_name)
        self.update_color_display()
        
    def update_color_display(self):
        """Update the color display canvas"""
        color_hex = C64_COLORS[self.current_color.get()]
        self.color_display.configure(bg=color_hex)
        
    def update_color_scheme_ui(self, parent):
        """Update the color scheme selector UI based on current mode"""
        # Clear existing widgets
        for widget in parent.winfo_children():
            widget.destroy()
        
        self.color_selectors = {}
        self.color_buttons = {}
        
        mode = self.color_mode.get()
        
        if mode == "HI-RES":
            labels = ["BG", "Block"]
        else:  # MULTI-COLOR
            labels = ["BG", "C1", "C2", "C3"]
        
        colors = self.selected_colors[mode]
        
        for idx, label in enumerate(labels):
            frame = ttk.Frame(parent)
            frame.pack(side=tk.LEFT, padx=2)
            
            ttk.Label(frame, text=label + ":", font=("Arial", 8)).pack(side=tk.LEFT, padx=1)
            
            # Color display button (smaller)
            color_name = colors[idx] if idx < len(colors) else "Black"
            color_hex = C64_COLORS[color_name]
            
            btn = tk.Canvas(frame, width=30, height=20, bg=color_hex, relief=tk.RAISED, bd=1)
            btn.pack(side=tk.LEFT, padx=1)
            self.color_buttons[idx] = btn
            
            # Set button to open color picker
            btn.bind("<Button-1>", lambda e, i=idx: self.pick_color_for_slot(i))
    
    def pick_color_for_slot(self, slot_idx):
        """Open color picker for a specific slot"""
        # Create a simple dialog to select color
        dialog = tk.Toplevel(self.root)
        dialog.title(f"Select Color for Slot {slot_idx}")
        dialog.geometry("400x400")
        
        def select_and_close(color_name):
            mode = self.color_mode.get()
            self.selected_colors[mode][slot_idx] = color_name
            # Store reference to scheme frame for update
            self.update_color_scheme_ui(self.scheme_frame)
            dialog.destroy()
            self.refresh_editor()
        
        scrollable = ttk.Frame(dialog)
        scrollable.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        for color_name, color_hex in C64_COLORS.items():
            btn = tk.Canvas(scrollable, width=350, height=25, bg=color_hex, relief=tk.RAISED, bd=1)
            btn.pack(fill=tk.X, pady=1)
            btn.bind("<Button-1>", lambda e, cn=color_name: select_and_close(cn))
            btn.create_text(175, 12, text=color_name, font=("Arial", 10),
                           fill="white" if self.is_dark(color_hex) else "black")
    
    def on_color_mode_changed(self):
        """Handle color mode change"""
        self.update_color_scheme_ui(self.scheme_frame)
        self.refresh_editor()
        
    def get_allowed_colors(self):
        """Get list of allowed colors for current mode"""
        mode = self.color_mode.get()
        return self.selected_colors[mode]
        
    def on_tile_size_changed(self):
        """Handle tile size change"""
        self.create_new_tile()
        
    def create_new_tile(self):
        """Create a new tile"""
        tile_data = {}
        self.tiles.append(tile_data)
        self.pixel_data[len(self.tiles) - 1] = {}
        self.current_tile_index = len(self.tiles) - 1
        self.update_tile_list()
        self.refresh_editor()
        
    def delete_tile(self):
        """Delete current tile"""
        if len(self.tiles) <= 1:
            messagebox.showwarning("Warning", "Must keep at least one tile")
            return
        self.tiles.pop(self.current_tile_index)
        # Update pixel_data keys
        new_pixel_data = {}
        for i, (k, v) in enumerate(self.pixel_data.items()):
            if k != self.current_tile_index:
                new_pixel_data[len(new_pixel_data)] = v
        self.pixel_data = new_pixel_data
        self.current_tile_index = max(0, self.current_tile_index - 1)
        self.update_tile_list()
        self.refresh_editor()
        
    def clear_tile(self):
        """Clear current tile"""
        self.pixel_data[self.current_tile_index] = {}
        self.refresh_editor()
        
    def copy_tile(self):
        """Copy the current tile and add as a new tile"""
        # Copy pixel data from current tile
        current_pixels = self.pixel_data[self.current_tile_index].copy()
        
        # Create new tile with copied data
        tile_data = {}
        self.tiles.append(tile_data)
        self.pixel_data[len(self.tiles) - 1] = current_pixels
        self.current_tile_index = len(self.tiles) - 1
        self.update_tile_list()
        self.refresh_editor()
        
    def on_onion_skin_changed(self, event):
        """Handle onion skin combobox selection"""
        value = event.widget.get()
        if value == "Previous Tile":
            self.onion_skin_tile_index.set(-1)
        else:
            # Extract tile number from "Tile N" format
            tile_num = int(value.split()[-1]) - 1
            self.onion_skin_tile_index.set(tile_num)
        self.refresh_editor()
        
    def on_tile_selected(self, event):
        """Handle tile selection from listbox"""
        selection = self.tile_listbox.curselection()
        if selection:
            self.current_tile_index = selection[0]
            self.refresh_editor()
            
    def update_tile_list(self):
        """Update the tile listbox"""
        self.tile_listbox.delete(0, tk.END)
        for i in range(len(self.tiles)):
            self.tile_listbox.insert(tk.END, f"Tile {i + 1}")
        self.tile_listbox.selection_set(self.current_tile_index)
        
    def on_canvas_click(self, event):
        """Handle canvas click for drawing"""
        self.paint_pixel(event)
        
    def on_canvas_drag(self, event):
        """Handle canvas drag for drawing"""
        self.paint_pixel(event)
        
    def on_canvas_right_click(self, event):
        """Handle right click for erasing"""
        self.paint_pixel(event, erase=True)
        
    def paint_pixel(self, event, erase=False):
        """Paint a pixel on the tile"""
        size = self.tile_size.get()
        zoom = self.zoom_level.get()
        pixel_x = event.x // zoom
        pixel_y = event.y // zoom
        
        if 0 <= pixel_x < size and 0 <= pixel_y < size:
            tile_pixels = self.pixel_data[self.current_tile_index]
            if erase:
                tile_pixels.pop((pixel_x, pixel_y), None)
            else:
                current_color = self.current_color.get()
                # Check if color is in allowed palette for this mode
                allowed_colors = self.get_allowed_colors()
                if current_color in allowed_colors:
                    tile_pixels[(pixel_x, pixel_y)] = C64_COLORS[current_color]
                else:
                    # Switch to first allowed color if current is not allowed
                    self.current_color.set(allowed_colors[0])
                    tile_pixels[(pixel_x, pixel_y)] = C64_COLORS[allowed_colors[0]]
            self.refresh_editor()
            
    def refresh_editor(self, *args):
        """Refresh the editor display"""
        size = self.tile_size.get()
        zoom = self.zoom_level.get()
        
        # Create image with selected background color
        tile_pixels = self.pixel_data[self.current_tile_index]
        background_color_name = self.selected_colors[self.color_mode.get()][0]
        background_color = C64_COLORS[background_color_name]
        img = Image.new("RGB", (size, size), background_color)
        
        # Draw onion skin if enabled
        if self.onion_skin_enabled.get():
            onion_index = self.onion_skin_tile_index.get()
            if onion_index == -1:
                # Show previous tile
                onion_index = self.current_tile_index - 1
            
            if 0 <= onion_index < len(self.tiles) and onion_index != self.current_tile_index:
                onion_pixels = self.pixel_data.get(onion_index, {})
                onion_img = Image.new("RGB", (size, size), background_color)
                for (x, y), color in onion_pixels.items():
                    if 0 <= x < size and 0 <= y < size:
                        onion_img.putpixel((x, y), tuple(int(color[i:i+2], 16) for i in (1, 3, 5)))
                # Blend onion skin at 30% opacity
                onion_img.putalpha(int(255 * 0.3))
                img = Image.alpha_composite(img.convert("RGBA"), onion_img.convert("RGBA")).convert("RGB")
        
        # Draw current tile pixels
        for (x, y), color in tile_pixels.items():
            if 0 <= x < size and 0 <= y < size:
                img.putpixel((x, y), tuple(int(color[i:i+2], 16) for i in (1, 3, 5)))
        
        # Zoom and add grid
        zoomed = img.resize((size * zoom, size * zoom), Image.NEAREST)
        draw = ImageDraw.Draw(zoomed)
        
        # Draw grid
        for i in range(size + 1):
            draw.line([(i * zoom, 0), (i * zoom, size * zoom)], fill=(100, 100, 100))
            draw.line([(0, i * zoom), (size * zoom, i * zoom)], fill=(100, 100, 100))
        
        self.editor_photo = ImageTk.PhotoImage(zoomed)
        self.editor_canvas.delete("all")
        self.editor_canvas.create_image(0, 0, image=self.editor_photo, anchor="nw")
        
        # Update stats
        pixel_count = len(tile_pixels)
        self.stats_label.config(text=f"Tile Size: {size}x{size}\nZoom: {zoom}x\nPixels: {pixel_count}/{size*size}\nTile: {self.current_tile_index + 1}/{len(self.tiles)}")
        
    def toggle_animation(self):
        """Start/stop animation"""
        self.is_animating = not self.is_animating
        self.animate_btn.config(text="⏸ Stop" if self.is_animating else "▶ Play")
        if self.is_animating:
            self.animate()
            
    def animate(self):
        """Animate tiles in preview"""
        if not self.is_animating:
            return
            
        size = self.tile_size.get()
        frame_index = getattr(self, '_frame_index', 0)
        
        # Get tile data and use selected background color
        tile_pixels = self.pixel_data[frame_index % len(self.tiles)]
        background_color_name = self.selected_colors[self.color_mode.get()][0]
        background_color = C64_COLORS[background_color_name]
        img = Image.new("RGB", (size, size), background_color)
        
        for (x, y), color in tile_pixels.items():
            if 0 <= x < size and 0 <= y < size:
                img.putpixel((x, y), tuple(int(color[i:i+2], 16) for i in (1, 3, 5)))
        
        # Scale for preview (fit in 300x300)
        scale = min(300 // size, 20)
        scaled = img.resize((size * scale, size * scale), Image.NEAREST)
        self.preview_photo = ImageTk.PhotoImage(scaled)
        self.preview_canvas.delete("all")
        self.preview_canvas.create_image(150, 150, image=self.preview_photo, anchor="center")
        
        self._frame_index = frame_index + 1
        self.root.after(self.animation_speed.get(), self.animate)
        
    def save_project(self):
        """Save project to file"""
        filename = filedialog.asksaveasfilename(defaultextension=".c64", filetypes=[("C64 Projects", "*.c64"), ("All Files", "*.*")])
        if filename:
            data = {
                "tile_size": self.tile_size.get(),
                "color_mode": self.color_mode.get(),
                "selected_colors": self.selected_colors,
                "tiles_count": len(self.tiles),
                "pixel_data": {str(k): {str(pos): color for pos, color in v.items()} for k, v in self.pixel_data.items()}
            }
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            messagebox.showinfo("Success", f"Project saved to {filename}")
            
    def load_project(self):
        """Load project from file"""
        filename = filedialog.askopenfilename(filetypes=[("C64 Projects", "*.c64"), ("All Files", "*.*")])
        if filename:
            with open(filename, 'r') as f:
                data = json.load(f)
            self.tile_size.set(data["tile_size"])
            
            # Load color mode and scheme if present (for backwards compatibility)
            if "color_mode" in data:
                self.color_mode.set(data["color_mode"])
                self.selected_colors = data.get("selected_colors", self.selected_colors)
            
            self.tiles = [{} for _ in range(data["tiles_count"])]
            self.pixel_data = {}
            for k_str, v in data["pixel_data"].items():
                k = int(k_str)
                self.pixel_data[k] = {eval(pos): color for pos, color in v.items()}
            self.current_tile_index = 0
            
            # Update color scheme UI
            self.update_color_scheme_ui(self.scheme_frame)
            
            self.update_tile_list()
            self.refresh_editor()
            messagebox.showinfo("Success", f"Project loaded from {filename}")


if __name__ == "__main__":
    root = tk.Tk()
    app = C64TileAnimator(root)
    root.mainloop()
