# C64 Tile Animator

A Python GUI tool for creating and animating Commodore 64 character tiles with authentic C64 colors.

## Features

- **Multiple Tile Sizes**: Support for 8x8, 16x16, and 32x32 pixel tiles
- **Authentic C64 Colors**: Full 16-color C64 palette
- **Color Modes**: 
  - **HI-RES Mode** - 2 colors (Background + Block color)
  - **MULTI-COLOR Mode** - 4 colors (Background + 3 colors)
- **Tile Editor**: Paint tiles with an intuitive pixel-by-pixel editor
- **Animation Preview**: Watch your tiles animate in real-time
- **Multiple Tiles**: Create sequences of tiles and animate them frame-by-frame
- **Zoom Levels**: Adjust zoom from 4x to 32x for precise editing
- **Project Management**: Save and load projects in .c64 format
- **Animation Controls**: Adjustable animation speed (10-500ms per frame)

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone or download this project
2. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

```bash
python c64_tile_animator.py
```

### How to Use

1. **Select Tile Size**: Choose between 8x8, 16x16, or 32x32 pixel tiles

2. **Choose Color Mode**: Select either HI-RES (2 colors) or MULTI-COLOR (4 colors)

3. **Configure Colors**: Select colors for your scheme:
   - HI-RES: Background + Block Color
   - MULTI-COLOR: Background + 3 colors

4. **Choose a Color**: Click on any color in your scheme to select it

5. **Draw Tiles**: 
   - **Left Click & Drag**: Paint pixels with the selected color
   - **Right Click & Drag**: Erase pixels
   - Use the Zoom slider to adjust how large the grid appears for easier editing

4. **Create Multiple Frames**:
   - Click "+ New" to create another tile
   - Create a sequence of tiles to form an animation

5. **Preview Animation**:
   - Adjust the animation speed (in milliseconds)
   - Click "▶ Play" to start the animation
   - Watch the tiles cycle in the preview panel on the right

6. **Manage Tiles**:
   - Select tiles from the Tile List to edit them
   - Click "- Delete" to remove the current tile (keep at least one)
   - Click "Clear" to erase all pixels from the current tile

7. **Save Your Work**:
   - Click "Save" to save your project as a .c64 file
   - Click "Load" to open a previously saved project

## Color Palette

The tool includes the authentic Commodore 64 16-color palette:

- Black, White, Red, Cyan
- Purple, Green, Blue, Yellow
- Orange, Brown, Light Red, Dark Gray
- Gray, Light Green, Light Blue, Light Gray

## Tips & Tricks

- **Fast Painting**: Hold down the mouse button and drag to paint multiple pixels at once
- **Quick Zoom**: Use the slider to zoom in for detailed work or zoom out to see the full tile
- **Animation Speed**: Lower values (10-50ms) create faster animations, higher values (200-500ms) create slower animations
- **Tile Sequences**: Create character animation sequences by designing multiple related tiles

## File Format

Projects are saved as JSON files with a .c64 extension. They contain:
- Tile size setting
- Number of tiles
- Pixel data for each tile (coordinates and colors)

You can open these files with any text editor to view or manually edit the data if needed.

## Keyboard/Mouse Reference

| Action | Control |
|--------|---------|
| Paint Pixel | Left Click & Drag |
| Erase Pixel | Right Click & Drag |
| Select Color | Click Color in Palette |
| Select Tile | Click in Tile List |
| Adjust Zoom | Zoom Slider |
| Play/Stop Animation | "▶ Play" / "⏸ Stop" Button |

## Future Enhancements

Potential features for future versions:
- Color picker from screen
- Flip/Rotate tools
- Copy/Paste tiles
- Undo/Redo functionality
- Export to various image formats
- Sprite sheet generation

## License

Free to use for personal and educational purposes.

Enjoy animating your C64 characters! 🎮✨
