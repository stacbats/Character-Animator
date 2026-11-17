# C64 Tile Animator - Features & Capabilities

## Core Features

### 🎨 Tile Editor
- **Multiple Sizes**: 8x8, 16x16, and 32x32 pixel tiles
- **Pixel-by-Pixel Editing**: Left-click to paint, right-click to erase
- **Zoom Control**: 4x to 32x magnification for precise work
- **Grid Display**: Visual grid helps with pixel alignment
- **Real-time Preview**: See changes instantly as you work

### 🎬 Animation System
- **Multiple Frames**: Create unlimited tiles/frames for animations
- **Adjustable Speed**: 10-500ms per frame control
- **Live Preview**: Watch animations play in real-time (300x300 preview panel)
- **Frame-by-Frame**: Click through tiles to edit individual frames

### 🎯 C64 Color Palette
Complete authentic 16-color Commodore 64 palette:
- **Primary Colors**: Black, White, Red, Cyan, Purple, Green, Blue, Yellow
- **Extended Colors**: Orange, Brown, Light Red, Dark Gray, Gray, Light Green, Light Blue, Light Gray

### 💾 Project Management
- **Save Projects**: Export as .c64 JSON files
- **Load Projects**: Import previously saved work
- **Persistent Data**: All pixel colors and positions preserved
- **Portable Format**: JSON files can be backed up or shared

### 📊 Information Display
- Real-time statistics showing:
  - Current tile size
  - Current zoom level
  - Number of pixels used
  - Current tile/total tiles

---

## User Interface Components

### Left Panel - Controls & Tools

**Tile Size Selection**
- Radio buttons for 8x8, 16x16, 32x32
- Instant tile creation on size change

**Zoom Level**
- Slider control (4x to 32x)
- Real-time zoom adjustment
- Current zoom level display

**Color Palette**
- Scrollable list of 16 C64 colors
- Color names for reference
- Visual color swatches
- Selected color highlighted

**Selected Color Display**
- Large color preview box
- Shows currently selected color
- 50x50 pixel preview area

**Animation Controls**
- Speed slider (10-500ms)
- Play/Stop button
- Current animation status display

**Tile Management**
- "+ New" button - Create new tile
- "- Delete" button - Remove current tile
- "Clear" button - Erase tile pixels
- Tile List (Listbox) - Select and navigate tiles

**File Operations**
- "Save" button - Export project
- "Load" button - Import project

### Center Area - Tile Editor Canvas
- Large editable canvas for the main tile
- Shows grid lines for pixel alignment
- Zoom-adjusted display
- Interactive painting surface

### Right Panel - Animation Preview
- **Preview Canvas**: Shows animation playback
- **Statistics**: Tile info and status
- **Dynamic Updates**: Changes reflect in real-time

---

## Workflow Examples

### Example 1: Creating a Walking Animation (8x8)
1. Set tile size to 8x8
2. Create Tile 1 - character with left leg forward
3. Create Tile 2 - character with neutral stance
4. Create Tile 3 - character with right leg forward
5. Set speed to 100ms
6. Play animation - character walks!

### Example 2: Blinking Character (16x16)
1. Set tile size to 16x16
2. Set zoom to 20x for detailed work
3. Create Tile 1 - character with open eyes
4. Create Tile 2 - character with winking eye
5. Create Tile 3 - character with closed eyes
6. Create Tile 4 - character with open eyes (loop back)
7. Set speed to 150ms
8. Play animation - character blinks

### Example 3: Color-Cycling Effect (32x32)
1. Set tile size to 32x32
2. Create multiple tiles with same pattern
3. Change colors on each frame progressively
4. Set speed to 50ms (fast)
5. Play animation - creates illusion of motion

---

## Technical Specifications

### Supported Tile Dimensions
- **8x8**: Classic C64 character size (64 pixels max)
- **16x16**: Double resolution (256 pixels max)
- **32x32**: High detail (1024 pixels max)

### Color Format
- RGB Hex format (#RRGGBB)
- Native C64 palette colors
- Lossless color preservation

### File Format
- JSON-based .c64 format
- Human-readable structure
- Portable between systems
- Easily parseable by external tools

### Performance
- Smooth real-time editing
- Fast tile switching
- Responsive animations
- Efficient memory usage

---

## Keyboard & Mouse Controls

| Input | Action |
|-------|--------|
| Left Click + Drag | Paint pixels |
| Right Click + Drag | Erase pixels |
| Click Color Swatch | Select color |
| Click Tile in List | Switch to tile |
| Drag Zoom Slider | Adjust magnification |
| Drag Speed Slider | Adjust animation speed |
| Click "+ New" | Add new tile |
| Click "▶ Play" | Start animation |
| Click "⏸ Stop" | Stop animation |

---

## Tips for Best Results

### Pixel Perfect Editing
- Use high zoom levels (20x-32x) for detailed work
- Use grid lines for alignment
- Take breaks to view at normal zoom

### Color Selection
- Use high contrast colors for small tiles
- Limit palette to 2-3 colors for 8x8 tiles
- Use all 16 colors for large 32x32 designs

### Animation Smoothness
- Create 4-8 frames for smooth motion
- Minimal changes between frames
- Use consistent timing (same speed for all tiles)

### File Management
- Save frequently during work
- Use descriptive file names
- Keep backup copies of important projects

---

## Limitations & Known Behaviors

✓ **Works Well With**
- 8x8 tiles (traditional C64 characters)
- 3-8 frame animations (smooth playback)
- Simple geometric designs
- Color-based patterns

⚠️ **Best Practices**
- Keep designs simple for 8x8 tiles
- Use distinct colors for clarity
- Test animation speed before saving
- Save frequently

---

## Future Enhancement Ideas

Planned features for upcoming versions:
- Undo/Redo functionality (Ctrl+Z/Ctrl+Y)
- Clipboard operations (Ctrl+C/Ctrl+V)
- Tile transformation tools (Flip, Rotate)
- Color picker from screen
- Sprite sheet export
- Animation frame preview strip
- Keyboard shortcuts for common tasks
- Tile duplication
- Multi-tile selection
- Layer support
- Custom grid options
- Pixel selection and move tools
- Filled shape tools (rectangle, circle)
- Paint bucket/fill tool
- Gradient tools

---

## Troubleshooting

**Q: Animation won't play**
A: Make sure you've created at least 2 tiles and clicked the Play button

**Q: Can't paint anything**
A: Ensure you've selected a color (not black) and you're clicking in the editor area

**Q: File won't save**
A: Check that the directory is writable and you have sufficient disk space

**Q: Zoom is too small**
A: Drag the Zoom slider to the right to increase magnification

**Q: Animation speed is wrong**
A: Adjust the speed slider - lower values = faster, higher values = slower

---

**Version**: 1.0.0
**Last Updated**: 2024
**License**: Free to use
