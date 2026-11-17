# C64 Tile Animator - Complete User Guide

## 📖 Table of Contents

1. [Quick Start](#quick-start)
2. [Installation](#installation)
3. [Interface Overview](#interface-overview)
4. [Creating Your First Tile](#creating-your-first-tile)
5. [Animation Basics](#animation-basics)
6. [Advanced Features](#advanced-features)
7. [Tips & Tricks](#tips--tricks)
8. [File Management](#file-management)
9. [Troubleshooting](#troubleshooting)
10. [Examples](#examples)

---

## Quick Start

### Windows Users
Double-click `run.bat` - That's it! ⚡

### macOS/Linux Users
```bash
chmod +x run.sh
./run.sh
```

### Manual Start
```bash
pip install -r requirements.txt
python c64_tile_animator.py
```

---

## Installation

### Requirements
- Python 3.7 or higher
- 50 MB free disk space
- 512 MB RAM minimum

### Full Installation Guide
See [INSTALL.md](INSTALL.md) for detailed instructions for your OS.

---

## Interface Overview

The application is divided into three main sections:

```
┌─────────────────────────────────────────────────────────────────┐
│                     C64 Tile Animator                            │
├──────────────────┬──────────────────────────┬──────────────────┤
│                  │                          │                  │
│   CONTROLS       │    TILE EDITOR          │   PREVIEW        │
│   (Left Panel)   │    (Center Panel)       │   (Right Panel)  │
│                  │                          │                  │
│ • Tile Size      │  - Main Editing Grid   │ • Animation      │
│ • Zoom Level     │  - Pixel-by-Pixel      │   Preview        │
│ • Color Palette  │    Drawing             │ • Statistics     │
│ • Animation      │  - Grid Lines          │                  │
│   Speed          │  - Zoomed View         │                  │
│ • Tiles List     │                        │                  │
│ • File Ops       │                        │                  │
│                  │                        │                  │
└──────────────────┴──────────────────────────┴──────────────────┘
```

### Left Panel - Controls

**Tile Size**
- Select 8x8, 16x16, or 32x32
- Automatically creates new tile when changed
- Classic C64 size is 8x8

**Color Mode** ⭐ NEW!
- Select **HI-RES (2 colors)** for classic look
- Select **MULTI-COLOR (4 colors)** for more detail
- Each mode has its own color scheme

**Color Scheme** ⭐ NEW!
- Configure colors for HI-RES mode:
  - Background (slot 1)
  - Block Color (slot 2)
- Configure colors for MULTI-COLOR mode:
  - Background (slot 1)
  - Color 1 (slot 2)
  - Color 2 (slot 3)
  - Color 3 (slot 4)
- Click color squares to change them
- Only selected colors appear in the palette below

**Zoom Level**
- Slider from 4x to 32x magnification
- Adjust for comfort and precision
- Higher zoom = bigger pixels

**Full Palette**
- Shows only colors from your current scheme
- Scroll to view all available colors
- Click to select
- Selected color shown below

**Animation Controls**
- Speed slider: 10-500ms per frame
- Lower = faster, Higher = slower
- Try 100-150ms for natural motion

**Tile Management**
- "+ New" - Add another tile/frame
- "- Delete" - Remove current tile (keep ≥1)
- "Clear" - Erase all pixels in tile
- Tile List - Select which tile to edit

**File Operations**
- "Save" - Export as .c64 file
- "Load" - Import from .c64 file

### Center Panel - Editor

Your main workspace for creating tiles:
- **Grid squares** = individual pixels
- **Grid lines** = pixel boundaries
- **Left-click + drag** = Paint
- **Right-click + drag** = Erase
- **Zoom slider** adjusts size

### Right Panel - Preview

Shows what your animation looks like:
- Displays current animation frame
- Shows file size and statistics
- Current tile number and total tiles
- Used pixel count

---

## Creating Your First Tile

### Step 1: Choose Tile Size
1. Look at "Tile Size" on left panel
2. Click the radio button for your size:
   - **8x8** - Classic and simple
   - **16x16** - More detail
   - **32x32** - Maximum detail
3. The editor updates automatically

**Recommendation**: Start with 8x8!

### Step 2: Select a Color
1. Find "Color Palette" section
2. Scroll through the colors
3. Click on a color like "Light Green" or "Cyan"
4. You'll see it highlighted in the "Selected" box

**Tip**: Avoid pure black if your background will be black

### Step 3: Paint Your Tile
1. Look at the editor grid in the center
2. Click and **drag** to paint pixels
3. **Right-click and drag** to erase
4. Build your design

**Example**: 8x8 smiling face
```
  . . # # . . . .
  . # . . # . . .
  # . . . . # . .
  # . . . . # . .
  . # . . # . . .
  . . # # . . . .
  . . . . . . . .
  . . . . . . . .
```

### Step 4: Preview Your Work
- Look at the right panel
- It shows the actual size (non-zoomed)
- Adjust colors if needed
- Use "Clear" to restart if unhappy

---

## Animation Basics

### Creating Multiple Frames

An animation is just several tiles shown in sequence:

1. **Paint Frame 1**
   - Click on the grid
   - Create your first image

2. **Click "+ New"**
   - Adds another blank tile
   - You'll see it in the "Tile List"

3. **Paint Frame 2**
   - Similar to Frame 1 but slightly different
   - Maybe slightly moved or changed expression

4. **Repeat**
   - Add Frame 3, 4, etc.
   - 3-4 frames usually looks good

### Playing Your Animation

1. **Set the Speed**
   - Drag "Animation Speed" slider
   - Try 100-150ms initially
   - Faster: lower value (50ms)
   - Slower: higher value (200ms)

2. **Click "▶ Play"**
   - Animation starts in preview panel
   - Cycles through all tiles
   - Button changes to "⏸ Stop"

3. **Watch the Preview**
   - Right panel shows animation
   - Tiles loop continuously
   - Adjust speed if needed

4. **Click "⏸ Stop"**
   - Stops the animation

### Animation Tips

**Smooth Motion**
- Minimal change between frames
- 3-5 frames minimum
- 100-150ms works for most cases

**Faster Animation**
- Lower speed value (50-75ms)
- Good for rapid effects
- Example: Blinking eyes

**Slower Animation**
- Higher speed value (200-300ms)
- Good for deliberate movements
- Example: Character walking

**Looping**
- Last frame automatically loops to first
- Design last frame with this in mind
- Smoother if first ≈ last frame

---

## Advanced Features

### Zoom Levels

The zoom slider lets you view at different magnifications:

| Zoom | Use For |
|------|---------|
| 4-8x | See full tile, planning layout |
| 12-16x | Comfortable editing |
| 20-32x | Detailed pixel-perfect work |

**Tip**: Design at 12x, then zoom to 24x for final touches

### Multiple Tiles

The "Tile List" on the left shows all your tiles:

**Select Tile**
- Click tile name in list
- Editor shows that tile
- Modify as needed

**Add Tile**
- Click "+ New"
- Blank tile added
- Automatically selected

**Delete Tile**
- Select tile in list
- Click "- Delete"
- Must keep at least 1 tile

**Clear Tile**
- Select tile in list
- Click "Clear"
- Erases all pixels in tile
- Tile still exists (empty)

### Color Selection

**Available Colors** (Authentic C64):
1. Black - Use for background (usually)
2. White - High contrast
3. Red - Bold color
4. Cyan - Light blue
5. Purple - Regal color
6. Green - Natural
7. Blue - Deep color
8. Yellow - Bright
9. Orange - Warm
10. Brown - Earthy
11. Light Red - Pink
12. Dark Gray - Muted black
13. Gray - Neutral
14. Light Green - Pastel
15. Light Blue - Sky
16. Light Gray - Very light

**Color Tips**:
- Use 2-3 colors max for 8x8 tiles
- High contrast colors look better small
- Color order matters for visual impact

---

## Tips & Tricks

### For 8x8 Tiles (Classic)

✓ Use bold colors (high contrast)
✓ Limit to 2-3 colors
✓ Simple geometric shapes
✓ Avoid fine details

**Example Colors**:
- Black + White + Yellow = Classic look
- Black + Cyan + Purple = Sci-fi look
- Black + Green + Yellow = Nature look

### For 16x16 Tiles (Medium)

✓ More detail possible
✓ Can use 4-5 colors
✓ Smooth curves possible
✓ Character portraits work well

### For 32x32 Tiles (Large)

✓ Maximum detail
✓ Use 5-8 colors
✓ Complex scenes
✓ Boss characters or environments

### Fast Painting Techniques

1. **Paint Multiple Pixels at Once**
   - Click and hold
   - Drag across multiple squares
   - Paints all squares you drag through

2. **Quick Erasing**
   - Right-click drag
   - Erases as you drag
   - Faster than painting with black

3. **Use Color Switching**
   - Click color
   - Paint
   - Click new color
   - Paint again
   - No need to clear between

4. **Zoom for Details**
   - Zoom to 24-32x
   - Paint small details
   - Zoom out to see result

---

## File Management

### Saving Projects

1. **Click "Save"** button
2. **Name your file**
   - Use descriptive name: "my_character.c64"
   - Avoid special characters
3. **Choose location**
   - Desktop (easy to find)
   - Documents (organized)
4. **File is saved**
   - .c64 extension added automatically
   - JSON format (readable text)

### Loading Projects

1. **Click "Load"** button
2. **Select file**
   - Browse to your .c64 file
   - Only .c64 files shown
3. **File opens**
   - All tiles restored
   - Tile size restored
   - Ready to continue editing

### File Format

.c64 files are JSON text:
```json
{
  "tile_size": 8,
  "tiles_count": 3,
  "pixel_data": {
    "0": { "(1,1)": "#70A4B2", ... },
    "1": { "(2,1)": "#FFFFFF", ... },
    "2": { "(3,1)": "#B8C76F", ... }
  }
}
```

**Can be opened with**:
- Notepad (view only)
- Any text editor
- The C64 Tile Animator (recommended)

### Backup Tips

1. **Save frequently** (every 5-10 minutes)
2. **Keep backups** (copy .c64 files elsewhere)
3. **Use versioning** (my_char_v1.c64, my_char_v2.c64)
4. **Cloud backup** (Dropbox, OneDrive, etc.)

---

## Troubleshooting

### Common Issues

**Can't paint**
→ Select a color (not black)
→ Make sure you're clicking in the grid

**Animation won't play**
→ Create at least 2 tiles
→ Click the Play button
→ Wait for animation to start

**Too slow to respond**
→ Close other programs
→ Reduce zoom level
→ Create smaller tiles

**File won't save**
→ Check folder permissions
→ Try a different folder (Desktop)
→ Make sure disk isn't full

**File won't load**
→ Ensure it's a .c64 file
→ Check if file is corrupted
→ Try opening with text editor

**Full troubleshooting**: See [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

---

## Examples

### Example 1: Blinking Character (8x8)

**Frame 1 - Eyes Open**
```
. # . . . . # .
# . # . . # . #
. # . . . . # .
. . . . . . . .
. # # # . # # .
# . . . . . . #
# . . . . . . #
. # # # . # # .
```

**Frame 2 - Eyes Closed**
```
. - . . . . - .
- . - . . - . -
. - . . . . - .
. . . . . . . .
. # # # . # # .
# . . . . . . #
# . . . . . . #
. # # # . # # .
```

**Speed**: 150ms, Loop for blinking effect

---

### Example 2: Walking Animation (8x8)

**Frame 1 - Left leg forward**
```
. . # # . . .
. . # # . . .
. # . . # . .
. # . . # . .
. # . . # . .
. . # . . . .
. . # # . . .
. . . # . . .
```

**Frame 2 - Neutral**
```
. . # # . . .
. . # # . . .
. # . . # . .
. # . . # . .
. # . . # . .
. . # . # . .
. . # . # . .
. . # # . . .
```

**Frame 3 - Right leg forward**
```
. . # # . . .
. . # # . . .
. # . . # . .
. # . . # . .
. # . . # . .
. . . . # . .
. . . # # . .
. . # . . . .
```

**Speed**: 100ms, Repeats for walking motion

---

### Example 3: Color Cycling (8x8)

**Frame 1** - Pattern in Red
**Frame 2** - Same pattern in Cyan  
**Frame 3** - Same pattern in Yellow
**Frame 4** - Same pattern in Purple

**Speed**: 50ms, Creates mesmerizing color rotation

---

## Keyboard Reference

| Input | Action |
|-------|--------|
| Left-Click Drag | Paint pixels |
| Right-Click Drag | Erase pixels |
| Click Color | Select color |
| Click Tile List | Switch tile |
| Drag Zoom | Adjust view |
| Click "+ New" | Add tile |
| Click "▶ Play" | Start animation |

---

## Need More Help?

- **Installation issues?** → [INSTALL.md](INSTALL.md)
- **Full features?** → [FEATURES.md](FEATURES.md)
- **Need quick start?** → [QUICKSTART.md](QUICKSTART.md)
- **Stuck?** → [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

---

## Happy Animating! 🎮✨

You're ready to create amazing C64 tiles and animations. 

Start with the sample_character.c64 file to see what's possible, then create your own!

Good luck with your retro game development! 🚀
