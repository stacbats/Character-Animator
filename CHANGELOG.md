# C64 Tile Animator - Version 1.1.0 Release Notes

## ✨ New Feature: Color Modes

We're excited to introduce **Color Modes** - a major new feature that makes the C64 Tile Animator even more authentic!

---

## What's New

### Color Mode Selection
Choose between two authentic C64 color modes:

#### 🎨 HI-RES Mode (2 Colors)
- Background + 1 Block Color
- Perfect for classic, simple sprites
- Maximum contrast and clarity
- Example: Black + White sprites

#### 🎨 MULTI-COLOR Mode (4 Colors)
- Background + 3 Additional Colors
- More detailed and expressive
- Perfect for game characters
- Example: Black + Red + Yellow + White

---

## How It Works

### 1. **Select Color Mode**
In the left panel under "Color Mode", choose:
- **HI-RES (2 colors)** - For simple designs
- **MULTI-COLOR (4 colors)** - For detailed designs

### 2. **Configure Your Color Scheme**
In the "Color Scheme" panel:
- Click the color squares to customize them
- Choose colors from the full C64 palette
- Settings saved with your project

### 3. **Paint Your Tile**
- The palette below only shows your selected colors
- Paint using just those colors
- Authentic C64 limitations enforced!

### 4. **Switch Modes Anytime**
- Change color mode at any time
- Color schemes for each mode are independent
- Existing pixels are preserved

---

## Key Features

✅ **Two Color Modes**
- HI-RES: 2 colors (authentic C64 high-res mode)
- MULTI-COLOR: 4 colors (authentic C64 multi-color mode)

✅ **Independent Color Schemes**
- Each mode has its own color palette
- Configure once, use many times
- Save/load with projects

✅ **Flexible Color Selection**
- Click to change any color slot
- Full 16-color palette available
- Instant preview

✅ **Backward Compatible**
- Old projects still load fine
- Defaults to MULTI-COLOR mode
- No data loss

---

## Usage Examples

### Example 1: HI-RES Character
```
Color Mode: HI-RES
Background: Black
Block Color: White

Result: Classic black & white pixel art
```

### Example 2: MULTI-COLOR Character
```
Color Mode: MULTI-COLOR
Background: Black
Color 1: Red (clothing)
Color 2: Yellow (hair)
Color 3: Cyan (eyes)

Result: Colorful character with personality
```

### Example 3: Animated Sequence with Color Changes
```
Frame 1: HI-RES, Black + White
Frame 2: HI-RES, Black + Yellow (different look)
Frame 3: HI-RES, Black + Cyan (another variation)

Animation: Character changes colors frame by frame!
```

---

## Updated Documentation

We've updated all documentation to include color modes:

- **[COLOR_MODES.md](COLOR_MODES.md)** - Complete color modes guide ⭐ START HERE
- **README.md** - Updated with color mode features
- **QUICKSTART.md** - Updated with color mode steps
- **GUIDE.md** - Detailed color mode sections

---

## User Interface Changes

### New Sections in Left Panel

**Before:**
```
├─ Tile Size
├─ Zoom Level
├─ Color Palette
└─ ... (rest of controls)
```

**After:**
```
├─ Tile Size
├─ Color Mode ⭐ NEW
├─ Color Scheme ⭐ NEW
├─ Zoom Level
├─ Full Palette
└─ ... (rest of controls)
```

---

## Technical Details

### Color Mode Storage
Projects now save with:
- Selected color mode (HI-RES or MULTI-COLOR)
- Color scheme for each mode
- All pixel data with actual hex colors

### Backward Compatibility
- Old .c64 files load without issues
- Defaults to MULTI-COLOR mode
- Color data preserved

### File Format
```json
{
  "tile_size": 8,
  "color_mode": "MULTI-COLOR",
  "selected_colors": {
    "HI-RES": ["Black", "White"],
    "MULTI-COLOR": ["Black", "White", "Red", "Cyan"]
  },
  "tiles_count": 3,
  "pixel_data": { ... }
}
```

---

## Getting Started with Color Modes

### Quick Start
1. Launch the app
2. Notice the new "Color Mode" section
3. Choose HI-RES or MULTI-COLOR
4. Click the color squares to customize
5. Paint your tile!

### Learning Path
1. Try HI-RES mode first (simpler)
2. Create a black & white character
3. Switch to MULTI-COLOR mode
4. Try a 4-color version
5. See which you prefer!

---

## Tips for Best Results

### HI-RES Mode (2 colors)
✓ Use high contrast colors
✓ Black + White = classic look
✓ Black + Yellow = arcade feel
✓ Perfect for simple sprites
✗ Avoid similar brightness colors

### MULTI-COLOR Mode (4 colors)
✓ Use 1 background + 3 accents
✓ Great for character details
✓ Background should be darkest
✓ Accents for clothing/features
✓ 3rd color for highlights

---

## Switching Between Modes

You can switch between modes for the same tile:

```
1. Create tile in HI-RES (Black + White)
2. Switch to MULTI-COLOR (Black + Red + Yellow + Cyan)
3. Paint with more colors
4. Switch back to HI-RES to see simplified version
5. Final version: Save in preferred mode!
```

---

## Saving Your First Color Mode Project

```bash
1. Create a tile in your preferred color mode
2. Click "Save" button
3. Enter filename: "my_colorful_character.c64"
4. Color mode and scheme are saved automatically!
5. Click "Load" later - everything restored perfectly
```

---

## Common Questions

**Q: Can I use the same colors in both modes?**
A: Yes! Configure colors independently for each mode.

**Q: What if I switch modes?**
A: Existing pixels are preserved. Just paint with new palette.

**Q: Can I undo a color mode change?**
A: Save before switching, then load the old version if needed.

**Q: Which mode is more authentic?**
A: Both! Real C64 had both HI-RES and MULTI-COLOR modes.

**Q: How many colors can I really use?**
A: 2 in HI-RES, 4 in MULTI-COLOR (including background).

---

## Comparison: Old vs New

| Aspect | Before | After |
|--------|--------|-------|
| Colors Available | 16 always | 2 or 4 per mode |
| Authenticity | Good | Excellent |
| Learning Curve | Easy | Simple |
| Flexibility | High | High + Authentic |
| File Size | Same | Same |
| Compatibility | - | Backward compatible |

---

## What's Coming Next?

Potential future features:
- Color palette presets (save/load custom schemes)
- Color optimization suggestions
- Multi-tile color scheme management
- Export color palettes
- Dither pattern support
- More color modes (bitmap, etc.)

---

## Troubleshooting

### Color palette doesn't show my color
**Solution**: That color isn't in your current scheme. Click the color scheme panel to add it.

### Colors changed when loading project
**Normal behavior**: Each mode has its own colors. Colors display correctly when loaded.

### Want different colors?
**Solution**: Click the color scheme panel color squares to customize them.

---

## Update Your Workflow

### Old Workflow:
```
1. Create tile
2. Paint with any of 16 colors
3. Save
```

### New Workflow (Recommended):
```
1. Choose color mode (HI-RES or MULTI-COLOR)
2. Configure color scheme
3. Create tile
4. Paint with selected colors
5. Save (mode & scheme included!)
```

---

## Migration Guide

### For Existing Projects
1. Load your old .c64 file
2. It opens in MULTI-COLOR mode (default)
3. All colors preserved!
4. Edit and re-save if desired

### For New Projects
1. Start fresh with new color mode selection
2. Configure your preferred palette
3. Create tiles
4. Everything is native color mode

---

## Thank You!

This feature was created to make the C64 Tile Animator even more authentic and useful for retro game development.

We hope you enjoy creating even more amazing C64 tiles! 🎮✨

---

## Resources

- **[COLOR_MODES.md](COLOR_MODES.md)** - Complete color modes documentation
- **[README.md](README.md)** - Full feature list
- **[QUICKSTART.md](QUICKSTART.md)** - Get started quickly
- **[GUIDE.md](GUIDE.md)** - Comprehensive guide

---

**Version**: 1.1.0  
**Release Date**: 2024  
**Feature**: Color Modes (HI-RES / MULTI-COLOR)  
**Status**: Stable

Happy creating! 🚀
