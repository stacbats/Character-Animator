# Color Modes Quick Visual Guide

## 🎨 HI-RES Mode (2 Colors)

### Layout
```
┌─────────────────────────────────────┐
│ Color Mode                          │
│ ○ HI-RES (2 colors) ← SELECT THIS  │
│ ○ MULTI-COLOR (4 colors)            │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ Color Scheme                        │
│ ┌──────────┐                        │
│ │Background│ ← Click to change     │
│ └──────────┘                        │
│   Black                             │
│                                     │
│ ┌──────────┐                        │
│ │Block Col.│ ← Click to change     │
│ └──────────┘                        │
│   White                             │
└─────────────────────────────────────┘
```

### Usage
- Background: Usually Black
- Block Color: Usually White, Yellow, Cyan, etc.
- Paint with just 2 colors total
- Result: Classic black & white sprites

### Examples
```
BLACK + WHITE         BLACK + YELLOW        BLACK + CYAN
█████                 ████░                 █░░░░
█   █                 █    ░                █░░░░
█ ░ █    becomes      █░░░░█      or       █░░░░█
█   █                 █░░░░█                █░░░░█
█████                 ████░█                █░░░█░
```

---

## 🎨 MULTI-COLOR Mode (4 Colors)

### Layout
```
┌─────────────────────────────────────┐
│ Color Mode                          │
│ ○ HI-RES (2 colors)                 │
│ ● MULTI-COLOR (4 colors) ← SELECT  │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ Color Scheme                        │
│ ┌──────────┐                        │
│ │Background│ ← Click to change     │
│ └──────────┘                        │
│   Black                             │
│                                     │
│ ┌──────────┐                        │
│ │ Color 1  │ ← Click to change     │
│ └──────────┘                        │
│   Red                               │
│                                     │
│ ┌──────────┐                        │
│ │ Color 2  │ ← Click to change     │
│ └──────────┘                        │
│   Yellow                            │
│                                     │
│ ┌──────────┐                        │
│ │ Color 3  │ ← Click to change     │
│ └──────────┘                        │
│   Cyan                              │
└─────────────────────────────────────┘
```

### Usage
- Background: Darkest color (usually Black)
- Color 1: Main color (clothing, body)
- Color 2: Accent color (hair, details)
- Color 3: Highlight color (eyes, shine)
- Paint with up to 4 colors total

### Examples
```
CHARACTER WITH 4 COLORS:

Frame with:          Looks like:
Black = background   ░░███░░
Red = clothing       ░██████
Yellow = hair        ██┌───┐██
Cyan = eyes          ██│●●│██
                     ░██└───┘██
                     ░░░███░░░
```

---

## 🔄 Switching Modes

### How to Switch
```
1. Click new color mode radio button
2. Configure colors (they appear in panel)
3. Start painting with new palette
4. All previous pixels preserved!
```

### Before & After

```
BEFORE: HI-RES (2 colors)
████████           Black
█      █
█  ██  █           White
█      █
████████

Switch to MULTI-COLOR, configure:
Background: Black, Color1: Red, 
Color2: Yellow, Color3: Cyan

AFTER: MULTI-COLOR (4 colors)
████████           Black
█════════█
█═══┌┐═══█         Red (═)
█════┘└═══█        Yellow (┌┐┘└)
████████           Cyan (dots inside)

Same pixels, more colorful!
```

---

## 🎯 Color Selection Process

### Step 1: Choose Mode
```
┌───────────────────────────┐
│ Color Mode                │
│ ⦿ MULTI-COLOR (4 colors)  │  ← Click radio button
│                           │
└───────────────────────────┘
```

### Step 2: Configure Colors
```
┌─────────────────────────────────────┐
│ Color Scheme                        │
│ ┌──────────┐                        │
│ │   ■ ■ ■  │ ← Click color square  │
│ └──────────┘                        │
│   Color Name                        │
└─────────────────────────────────────┘

Color Picker Opens:
┌───────────────────────────┐
│ Select Color for Slot 1   │
├───────────────────────────┤
│ ■ Black                   │
│ ■ White   ← Click          │
│ ■ Red                     │
│ ■ Cyan                    │
│ ... (all 16 colors)       │
└───────────────────────────┘
```

### Step 3: Paint
```
Full Palette Now Shows:
┌──────────────────────────┐
│ ■ Black (slot 1)         │
│ ■ White (slot 2)         │
│ ■ Red (slot 3)           │
│ ■ Cyan (slot 4)          │
│                          │
│ Other colors (not        │
│ available in this mode)  │
└──────────────────────────┘

Paint with selected colors! ← Paint with these only
```

---

## 📊 Comparison Table

| Feature | HI-RES | MULTI-COLOR |
|---------|--------|-------------|
| Colors | 2 | 4 |
| Background | ✓ | ✓ |
| Accent Colors | 1 | 3 |
| Complexity | Simple | Detailed |
| File Size | Small | Slightly larger |
| Authenticity | Classic | Authentic |
| Best For | Symbols | Characters |

---

## 🎨 Color Scheme Suggestions

### HI-RES: Classic Schemes
```
1. Black + White      ◼ ◻
2. Black + Yellow     ◼ ◾
3. Black + Cyan       ◼ ◽
4. Dark Gray + White  ▪ ▫
```

### MULTI-COLOR: Character Schemes
```
1. Modern Character
   Black + Brown + Yellow + Cyan
   ◼ + ◻ + ◾ + ◽

2. Neon Style
   Black + Cyan + Purple + White
   ◼ + ◽ + ◹ + ◻

3. Fire Effect
   Black + Red + Orange + Yellow
   ◼ + ◹ + ◸ + ◾

4. Nature
   Black + Green + Light Green + Brown
   ◼ + ◷ + ◺ + ◸
```

---

## 🎬 Animation with Color Modes

### Same Tiles, Different Colors Per Frame

```
Frame 1: Black + White
█████
█   █
█ ○ █
█   █
█████

Frame 2: Black + Yellow
█████
█   █
█ ● █
█   █
█████

Frame 3: Black + Cyan
█████
█   █
█ ◉ █
█   █
█████

Animation: Character blinks with color changes!
```

---

## 🔧 Troubleshooting Visual

### Problem: Color Not In Palette
```
Current Scheme Colors:
┌─────────────────┐
│ ■ Black         │
│ ■ White         │
│ ■ Red           │
│ ■ Cyan          │
└─────────────────┘

Want to use Green? Not here!

SOLUTION:
1. Click Color Scheme panel
2. Click Color 2 slot (Red)
3. Select Green from color picker
4. Now Green appears in palette!
```

### Problem: Switched Modes, Colors Changed
```
HI-RES: Black + White
        ██ ██
        █   █
        █ ○ █
        █   █
        ██ ██

Switch to MULTI-COLOR:
        ██ ██
        █   █
        █ ● █
        █   █
        ██ ██

New colors: Black + White + Red + Cyan
Same pixels, now with 4-color potential!
```

---

## 📱 Mobile/Small Screen View

If the UI feels cramped:
1. Maximize window
2. Or reduce zoom to see full layout
3. Or scroll the left panel

```
Recommended window size: 1200x850 pixels
Recommended zoom: 16-20x for editing
```

---

## ✨ Tips & Tricks

### Tip 1: Save Before Experimenting
```
1. Create tile in HI-RES
2. Save as "v1.c64"
3. Try MULTI-COLOR mode
4. If you don't like it, load "v1.c64"
```

### Tip 2: Use Same Colors for All Frames
```
Frame 1-4: Keep same colors
           Different patterns
Result:    Smooth animation with consistent colors
```

### Tip 3: Gradually Add Colors
```
Step 1: Create basic shape in HI-RES (2 colors)
Step 2: Switch to MULTI-COLOR (4 colors)
Step 3: Add color 2 and 3 for details
Result: Progressively more detailed character
```

### Tip 4: Preview in Different Modes
```
1. Design in MULTI-COLOR (4 colors)
2. Switch to HI-RES with best 2 colors
3. See how it simplifies
4. Decide which is better!
```

---

**Version**: 1.1.0  
**Visual Guide Created**: 2024

Enjoy your color modes! 🎨🎮✨
