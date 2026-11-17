# C64 Color Modes - Feature Guide

## Overview

The C64 Tile Animator now supports authentic Commodore 64 color modes:

- **HI-RES Mode** - 2 colors (Background + 1 Block color)
- **MULTI-COLOR Mode** - 4 colors (Background + 3 additional colors)

---

## Color Modes Explained

### HI-RES Mode (2 Colors)

**Use Case**: Classic high-resolution sprites with just 2 colors

**Colors Available**:
1. **Background** - The base color (usually Black)
2. **Block Color** - The main character/object color

**Example**: 
- Background: Black
- Block Color: White
- Result: Classic black & white sprites (like Pong or Space Invaders)

**Characteristics**:
- Sharp, clean look
- Maximum contrast
- Simple but effective
- Minimal file size
- Classic 1980s feel

---

### MULTI-COLOR Mode (4 Colors)

**Use Case**: More detailed sprites with richer color palette

**Colors Available**:
1. **Background** - Base color (usually Black)
2. **Color 1** - First accent color
3. **Color 2** - Second accent color
4. **Color 3** - Third accent color

**Example**:
- Background: Black
- Color 1: Red
- Color 2: Yellow
- Color 3: White
- Result: Colorful sprites (like classic game characters)

**Characteristics**:
- More expressive and detailed
- Better for characters with clothing/details
- More authentic to actual C64 graphics
- Richer visual appearance
- Still constrained (true C64 limitation)

---

## How to Use Color Modes

### Step 1: Select Color Mode

In the left panel under "Color Mode":
- Click **"HI-RES (2 colors)"** for 2-color mode
- Click **"MULTI-COLOR (4 colors)"** for 4-color mode

### Step 2: Configure Your Colors

A new "Color Scheme" panel appears below the color mode selection.

**For HI-RES**:
- Click the "Background" color square to change it
- Click the "Block Color" color square to change it

**For MULTI-COLOR**:
- Click any of the 4 color squares to customize that slot
- Background (slot 1)
- Color 1 (slot 2)
- Color 2 (slot 3)
- Color 3 (slot 4)

### Step 3: Paint Your Tile

The color palette on the left only shows colors from your selected scheme!

- Select a color from your scheme
- Paint your tile
- Only the 2 (or 4) colors are available to paint with

---

## Workflow Example: Creating a 2-Color Character

### HI-RES Mode Character

```
1. Set Color Mode to "HI-RES"
2. Leave Background as "Black"
3. Set Block Color to "White"
4. Paint your character using just Black and White
5. Watch it render with perfect contrast
```

### Result:
Classic black & white pixel art character.

---

## Workflow Example: Creating a 4-Color Character

### MULTI-COLOR Mode Character

```
1. Set Color Mode to "MULTI-COLOR"
2. Keep Background as "Black"
3. Set Color 1 to "Red" (for clothing/body)
4. Set Color 2 to "Yellow" (for hair/accent)
5. Set Color 3 to "Cyan" (for eyes/details)
6. Paint using these 4 colors
7. Character has much more detail and personality
```

### Result:
Rich, detailed character with 4-color palette (authentic C64 style).

---

## Benefits of Color Mode Selection

| Aspect | HI-RES | MULTI-COLOR |
|--------|--------|-------------|
| Colors | 2 | 4 |
| Simplicity | Very Simple | More Complex |
| File Size | Smaller | Slightly Larger |
| Visual Impact | High Contrast | More Detailed |
| Learning Curve | Easy | Moderate |
| Authenticity | Retro Simple | Classic C64 |

---

## Color Selection Tips

### HI-RES Best Practices

**High Contrast Pairs**:
- Black + White (maximum contrast)
- Black + Yellow (classic arcade)
- Black + Cyan (clean look)
- Dark Gray + Light Gray (retro computer feel)

**Avoid**:
- Similar brightness colors (hard to see)
- Too dark combinations

### MULTI-COLOR Best Practices

**Warm Palette** (reds/yellows/oranges):
- Background: Black
- Color 1: Brown
- Color 2: Orange
- Color 3: Yellow

**Cool Palette** (blues/cyans/purples):
- Background: Black
- Color 1: Dark Gray
- Color 2: Blue
- Color 3: Light Blue

**Character-Focused**:
- Background: Black
- Color 1: Skin tone (Brown/Orange)
- Color 2: Clothing (Blue/Red/Green)
- Color 3: Accent (Yellow/White)

---

## Switching Color Modes

You can switch between HI-RES and MULTI-COLOR at any time:

1. Select different mode
2. Configure new colors
3. Paint continues with new palette
4. All existing pixel data is preserved!

**Note**: If you have pixels painted with colors that aren't in the new mode, those pixels will be preserved in the saved file but won't display those exact colors when painted with the new mode.

---

## Saving & Loading

Color modes and schemes are automatically saved with your project:

**When you save:**
- Current color mode (HI-RES or MULTI-COLOR)
- All configured colors for both modes
- All pixel data with actual hex colors

**When you load:**
- Color mode is restored
- Color schemes are restored
- Tiles render exactly as saved

This means you can:
- Save multiple projects in different modes
- Switch between HI-RES and MULTI-COLOR projects
- Experiment with different color schemes for the same tile

---

## Authenticity to Actual C64

The Commodore 64 had different graphics modes:

- **HI-RES Mode**: Each character can be 2 colors (foreground + background)
- **MULTI-COLOR Mode**: Each character can be 4 colors (background + 3 colors)

This tool accurately reflects those constraints, letting you create authentic C64 graphics!

---

## Advanced Tips

### Switching Modes While Designing

You can switch between modes to see which looks better:

1. Create tile in MULTI-COLOR (4 colors)
2. Switch to HI-RES (2 colors)
3. Configure the 2 colors
4. See how it looks with limited palette
5. Switch back to add more colors if needed

### Creating Animated Sequences

Each frame can have its own color scheme:

1. Frame 1: HI-RES with Black + White
2. Click "+ New"
3. Frame 2: Keep HI-RES but switch to Black + Yellow
4. Animation cycles through different color schemes!

### Color Cycling Effects

MULTI-COLOR mode is perfect for color cycling:

1. Keep the same pattern on each frame
2. Change the 3 color slots on each frame
3. Set animation speed to 50ms
4. Watch the pattern animate through colors!

---

## Troubleshooting

### "My color isn't available"

**Problem**: Clicked a color but it doesn't appear on the palette

**Solution**: That color isn't in your current scheme. Click the color scheme button to change it.

---

### "I want to use a color not in the palette"

**Problem**: Want to use Orange but it's not available

**Solution**:
1. Find the color in "Full Palette" section
2. Click the color scheme button for that slot
3. Find and select the color you want

---

### "Colors switched when I changed modes"

**Problem**: Loading a project and colors look different

**Solution**: This is normal! Different modes have different color slots. Reload and it should display correctly.

---

## Examples in Gallery

The `sample_character.c64` file uses MULTI-COLOR mode with:
- Black background
- White, Red, and Cyan colors

Try loading it and switching to HI-RES mode to see the difference!

---

## Future Enhancements

Potential future features:
- Custom color palette editing
- Save color schemes as presets
- Export color palette as C64 assembly
- Color palette optimization
- Dither patterns for limited colors

---

**Version**: 1.1.0  
**Feature**: Color Modes (HI-RES / MULTI-COLOR)  
**Last Updated**: 2024

Enjoy creating authentic C64 graphics! 🎮✨
