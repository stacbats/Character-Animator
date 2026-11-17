# C64 Tile Animator - Project Overview

## 🎮 Welcome to C64 Tile Animator!

A complete Python GUI application for creating and animating Commodore 64 character tiles with authentic C64 colors.

---

## 📁 Project Files

### Main Application
- **[c64_tile_animator.py](c64_tile_animator.py)** (15 KB)
  - Main application with full GUI
  - Tile editor with drawing tools
  - Animation preview and playback
  - Project save/load functionality
  - ~400 lines of well-structured Python code

### Documentation
- **[README.md](README.md)** - Full feature documentation and usage guide
- **[QUICKSTART.md](QUICKSTART.md)** - Get started in 30 seconds
- **[INSTALL.md](INSTALL.md)** - Detailed installation instructions for all platforms
- **[FEATURES.md](FEATURES.md)** - Comprehensive feature breakdown and technical specs

### Configuration
- **[requirements.txt](requirements.txt)** - Python dependencies (just Pillow)

### Sample Data
- **[sample_character.c64](sample_character.c64)** - Example animated character to get you started

---

## 🚀 Quick Start

### 1. Install (One-time)
```bash
pip install -r requirements.txt
```

### 2. Run
```bash
python c64_tile_animator.py
```

### 3. Create
- Choose tile size (8x8, 16x16, or 32x32)
- Paint with C64 colors
- Create multiple frames
- Watch them animate!

---

## ✨ Key Features

✅ **Multiple Tile Sizes** - 8x8, 16x16, 32x32  
✅ **Authentic C64 Palette** - All 16 original colors  
✅ **Paint & Animate** - Create fluid animations frame-by-frame  
✅ **Real-time Preview** - Watch animations play instantly  
✅ **Zoom Control** - 4x to 32x magnification  
✅ **Save/Load** - Export projects as .c64 files  
✅ **User-Friendly GUI** - Intuitive controls and layout  

---

## 📚 Documentation Guide

| Document | Best For |
|----------|----------|
| **QUICKSTART.md** | I want to start immediately (5 min read) |
| **README.md** | I want complete feature overview (10 min read) |
| **INSTALL.md** | I'm having installation issues (varies) |
| **FEATURES.md** | I want detailed technical information (15 min read) |

---

## 🎨 What You Can Create

### 8x8 Tiles (Classic)
- Original Commodore 64 character size
- Perfect for retro game sprites
- Minimal animation (3-4 frames)
- Example: Running character, blinking eyes

### 16x16 Tiles (Medium)
- Double resolution for more detail
- Better for complex designs
- Smoother animations (5-8 frames)
- Example: Detailed character portrait, enemy variations

### 32x32 Tiles (Large)
- High detail capabilities
- Full animation sequences
- Complex scene elements
- Example: Boss character, detailed background tile

---

## 💾 Project Format

Projects are saved as `.c64` files (JSON format):
- Fully human-readable
- Portable between systems
- Can be edited manually if needed
- Includes all pixel data and colors

Example structure:
```json
{
  "tile_size": 8,
  "tiles_count": 3,
  "pixel_data": {
    "0": { "(1, 1)": "#70A4B2", ... },
    "1": { "(2, 1)": "#FFFFFF", ... },
    "2": { "(3, 1)": "#B8C76F", ... }
  }
}
```

---

## 🎯 Workflow Example

1. **Launch** the application
2. **Choose** an 8x8 tile size
3. **Paint** frame 1 of your character
4. **Click "+ New"** to add frame 2
5. **Paint** a variation
6. **Repeat** for frame 3-4
7. **Adjust** animation speed (try 100-150ms)
8. **Click "▶ Play"** to preview
9. **Save** your work as `my_character.c64`

---

## 🔧 Technical Specs

- **Language**: Python 3.7+
- **GUI Framework**: Tkinter (built-in)
- **Image Processing**: PIL/Pillow
- **File Format**: JSON (.c64 extension)
- **Platform Support**: Windows, macOS, Linux
- **Memory**: Lightweight (< 50 MB with dependencies)

---

## 📋 System Requirements

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| Python | 3.7 | 3.9+ |
| RAM | 512 MB | 2 GB |
| Disk Space | 50 MB | 100 MB |
| OS | Windows 10, macOS 10.14, Ubuntu 18.04 | Windows 11, macOS 12+, Ubuntu 20.04+ |

---

## 🎓 Learning Resources

### For Beginners
1. Read **QUICKSTART.md** (5 min)
2. Launch application
3. Try the included `sample_character.c64`
4. Follow the example workflow above

### For Advanced Users
1. Read **FEATURES.md** for all capabilities
2. Explore animation speed optimization
3. Create complex multi-frame sequences
4. Experiment with color combinations

### For Developers
- Main code is in `c64_tile_animator.py`
- Well-commented and modular design
- Easy to extend with new features
- Uses standard Python libraries

---

## 🛠️ Common Tasks

### Create a Walking Animation
1. Create 3-4 tiles with legs in different positions
2. Set speed to 100ms
3. Watch your character walk!

### Design a Character Portrait
1. Use 16x16 tile size
2. Zoom to 20x for detail work
3. Create 2-3 expression variations
4. Set speed to 200ms for slower animation

### Make a Color-Cycling Background
1. Use 32x32 tiles
2. Same pattern, different colors on each frame
3. Set speed to 50-75ms (fast!)
4. Creates smooth color rotation effect

---

## 📞 Support & Troubleshooting

**Installation Issues?** → See [INSTALL.md](INSTALL.md)

**Can't paint?** → Check you've selected a color (not black)

**Animation too fast?** → Increase speed value (200-300ms)

**File won't load?** → Ensure it's a valid .c64 file (JSON format)

**Other questions?** → Check [README.md](README.md) or [FEATURES.md](FEATURES.md)

---

## 🎮 C64 Color Palette Reference

The application includes these authentic Commodore 64 colors:

```
Black, White, Red, Cyan
Purple, Green, Blue, Yellow
Orange, Brown, Light Red, Dark Gray
Gray, Light Green, Light Blue, Light Gray
```

Perfect for creating authentic retro game graphics!

---

## 🚀 Future Enhancements

Planned features for upcoming versions:
- Undo/Redo (Ctrl+Z/Ctrl+Y)
- Clipboard support (Ctrl+C/Ctrl+V)
- Flip/Rotate tools
- Color picker
- Sprite sheet export
- Layer support
- Keyboard shortcuts

---

## 📄 Version Information

- **Current Version**: 1.0.0
- **Release Date**: 2024
- **License**: Free to use for personal and educational purposes
- **Status**: Stable and production-ready

---

## 🎉 Get Started Now!

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python c64_tile_animator.py
```

Then open **QUICKSTART.md** and follow the 30-second guide!

---

**Happy retro game development! 🎮✨**

For more information, see the documentation files listed above.
