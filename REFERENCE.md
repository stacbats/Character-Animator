# C64 Tile Animator - Quick Reference Card

## 🎮 Application Launch

| OS | Command |
|-------|---------|
| **Windows** | Double-click `run.bat` |
| **macOS/Linux** | `chmod +x run.sh && ./run.sh` |
| **Any OS** | `python c64_tile_animator.py` |

---

## 🎨 Main Controls

### Painting
| Mouse Action | Result |
|---|---|
| Left Click + Drag | Paint pixels |
| Right Click + Drag | Erase pixels |
| Click Color Swatch | Select color |

### UI Controls
| Button | Function |
|---|---|
| **Tile Size Radios** | 8x8 / 16x16 / 32x32 |
| **Zoom Slider** | 4x to 32x magnification |
| **Speed Slider** | 10-500ms per frame |
| **+ New** | Add new tile/frame |
| **- Delete** | Remove current tile |
| **Clear** | Erase all pixels in tile |
| **Save** | Export as .c64 file |
| **Load** | Import .c64 file |
| **▶ Play / ⏸ Stop** | Control animation |

---

## 🎨 C64 Color Palette

```
1. Black              9. Orange
2. White             10. Brown
3. Red               11. Light Red (Pink)
4. Cyan              12. Dark Gray
5. Purple            13. Gray
6. Green             14. Light Green
7. Blue              15. Light Blue
8. Yellow            16. Light Gray
```

**Tip**: Use high contrast colors for small tiles!

---

## 📐 Tile Sizes

| Size | Use Case | Max Pixels | Detail Level |
|------|----------|-----------|--------------|
| **8×8** | Classic sprites | 64 | Low (simple) |
| **16×16** | Medium detail | 256 | Medium |
| **32×32** | High detail | 1,024 | High (complex) |

---

## ⚙️ Recommended Settings

### For Quick Animations
- Tile Size: 8×8
- Zoom: 16×
- Speed: 100-150ms
- Frames: 3-4

### For Detailed Work
- Tile Size: 16×16
- Zoom: 20×
- Speed: 200ms
- Frames: 6-8

### For Maximum Detail
- Tile Size: 32×32
- Zoom: 24×
- Speed: 100-200ms
- Frames: 4-6

---

## 📁 File Management

### Saving
1. Click "Save" button
2. Enter filename (e.g., "my_character.c64")
3. Choose location (Desktop recommended)
4. File saved with all tiles

### Loading
1. Click "Load" button
2. Select a .c64 file
3. All tiles restored
4. Continue editing

### File Format
- **Extension**: .c64
- **Format**: JSON (text)
- **Portable**: Works anywhere
- **Editable**: Can view in text editor

---

## 🎬 Animation Workflow

```
1. Select tile size
2. Paint Frame 1
3. Click "+ New" for Frame 2
4. Paint Frame 2 (slight variation)
5. Repeat Steps 3-4 for more frames
6. Adjust "Animation Speed" slider
7. Click "▶ Play" to preview
8. Click "Save" to export
```

---

## ⏱️ Animation Speed Reference

| Speed (ms) | Animation Type | Example |
|-----------|---|---|
| **50-75** | Very fast | Blinking, effects |
| **100-150** | Normal | Walking, talking |
| **200-300** | Slow | Dramatic movement |
| **400-500** | Very slow | Transition effects |

**Lower = Faster** | **Higher = Slower**

---

## 🎯 Quick Tips

| Tip | Benefit |
|-----|---------|
| Use 8×8 for starting | Simple and classic |
| Zoom to 16-20× for work | Comfortable editing |
| Use 2-3 colors max on 8×8 | High contrast |
| Create 3-5 frames | Smooth animation |
| Test speed before saving | Perfect timing |
| Save frequently | Never lose work |
| Use backups | Extra safety |
| Use descriptive names | Easy to find files |

---

## 🎨 Color Combination Ideas

### Classic Games
- **Mario-style**: Red + Yellow + White
- **Pac-Man**: Yellow + Black + (Blue/Pink)
- **Space**: Cyan + White + Purple

### Modern Retro
- **Neon**: Cyan + Light Blue + Purple
- **Nature**: Green + Light Green + Brown
- **Fire**: Red + Orange + Yellow

### Abstract
- **Checkerboard**: Black + White
- **Rainbow**: 6-8 different colors
- **Sunset**: Orange + Yellow + Purple

---

## 📋 Keyboard/Mouse Cheat Sheet

| Input | Action | Result |
|-------|--------|--------|
| Left-Click | Select UI element | Activates control |
| Left-Drag on canvas | Paint pixels | Draws with current color |
| Right-Drag on canvas | Erase pixels | Removes pixels |
| Scroll in palette | View all colors | See more color options |
| Click in tile list | Switch tile | Edit different frame |
| Drag sliders | Adjust values | Change zoom/speed |

---

## 🆘 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| Can't paint | Select a color first |
| Animation won't play | Need at least 2 tiles |
| Animation too fast | Increase speed value |
| Animation too slow | Decrease speed value |
| File won't save | Try different folder |
| File won't load | Ensure it's a .c64 file |
| Window too small | Maximize or resize window |
| Colors invisible | Use high contrast colors |

**More help**: See TROUBLESHOOTING.md

---

## 📚 Documentation Map

| Need | Read |
|------|------|
| Quick start (5 min) | **QUICKSTART.md** |
| Complete guide (20 min) | **GUIDE.md** |
| All features | **FEATURES.md** |
| Installation help | **INSTALL.md** |
| Problem solving | **TROUBLESHOOTING.md** |
| Overview | **INDEX.md** or **START_HERE.md** |

---

## 🎮 Project Structure

```
Tile_Animator/
├── c64_tile_animator.py    ← Main application
├── requirements.txt         ← Dependencies
├── run.bat                  ← Windows launcher
├── run.sh                   ← Linux/macOS launcher
├── sample_character.c64     ← Example file
│
└── Documentation:
    ├── START_HERE.md        ← Begin here!
    ├── QUICKSTART.md        ← 5-minute guide
    ├── GUIDE.md             ← Full instructions
    ├── FEATURES.md          ← Technical details
    ├── INSTALL.md           ← Setup help
    ├── TROUBLESHOOTING.md   ← Problem solving
    ├── README.md            ← Overview
    └── INDEX.md             ← Project index
```

---

## ✨ Feature Checklist

✅ Draw 8×8, 16×16, or 32×32 tiles  
✅ 16-color authentic C64 palette  
✅ Paint and erase freely  
✅ Create multiple animation frames  
✅ Adjust animation speed  
✅ Real-time preview  
✅ Zoom from 4× to 32×  
✅ Save/load projects  
✅ Export as .c64 files  
✅ Works on Windows, macOS, Linux  

---

## 🚀 Getting Started

### Right Now
1. Run the application
2. Open sample_character.c64 to see example
3. Create a new 8×8 tile
4. Paint a simple design
5. Add 2 more frames
6. Click Play and watch!

### In 5 Minutes
Read QUICKSTART.md and follow the steps

### Complete Guide
Read GUIDE.md for everything

---

## 💾 Remember

- **Save often** (every 5-10 minutes)
- **Keep backups** (copy files elsewhere)
- **Use clear names** (my_char_v1.c64)
- **Test before saving** (animation speed, colors)
- **Have fun!** (this is creative!)

---

**Version**: 1.0.0 | **Status**: Ready to use | **License**: Free

**Happy animating! 🎮✨**
