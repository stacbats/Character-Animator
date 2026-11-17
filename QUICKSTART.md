# C64 Tile Animator - Quick Start Guide

## Get Started in 30 Seconds

### 1. Install Dependencies (One-time setup)
```bash
pip install -r requirements.txt
```

### 2. Launch the App
```bash
python c64_tile_animator.py
```

## 3. Create Your First Animated Tile

**Step 1: Select a Tile Size**
- Look at the top left under "Tile Size"
- Choose 8x8 (classic), 16x16 (medium), or 32x32 (large)
- Let's start with 8x8!

**Step 2: Choose a Color Mode**
- Look at "Color Mode" section (new!)
- **HI-RES (2 colors)**: Classic black & white look
- **MULTI-COLOR (4 colors)**: More colorful with 3 accent colors
- Start with HI-RES for simplicity

**Step 3: Configure Your Colors**
- Look at "Color Scheme" panel
- Click the color boxes to change them
- HI-RES has 2 slots: Background + Block Color
- Leave as Black + White to start

**Step 4: Pick a Color to Paint**
- Scroll through the "Full Palette" on the left
- Click on a color in your scheme
- You'll see it highlighted in the "Selected" box

**Step 5: Draw**
- In the big grid in the center (the "Tile Editor")
- Click and drag to paint pixels
- Right-click and drag to erase

**Step 6: Create Animation Frames**
- Click the "+ New" button to add another tile
- Paint a slightly different version of your character
- Repeat to create a sequence (3-4 frames usually looks good)

**Step 7: Preview Animation**
- Adjust "Animation Speed" - try 100ms to start
- Click the "▶ Play" button
- Watch your animation in the preview on the right! 🎬

**Step 8: Save Your Work**
- Click the "Save" button
- Give it a name like "my_character.c64"
- Later, click "Load" to open it again

---

## Example: Creating a Simple 8x8 Character

1. **New project opens** - Set to HI-RES with Black background and White block color
2. **Draw face frame 1**: 
   - Paint eyes with White (2 pixels)
   - Paint mouth with White (3-4 pixels)
3. **Click "+ New"** to add frame 2
4. **Draw face frame 2**: 
   - Same eyes
   - Different mouth (smile vs frown)
5. **Click "+ New"** to add frame 3
6. **Draw face frame 3**:
   - Closed eyes or wink
7. **Set speed to 150ms** (adjust slider)
8. **Click Play** - Your character blinks and changes expression!

---

## Zoom In for Detail Work

- If the pixels are too small, drag the **"Zoom Level"** slider to the right
- Higher zoom = bigger pixels = easier to edit
- 16x is usually perfect for 8x8 tiles

---

## Color Tips

**Classic C64 Looks:**
- **Mario-style**: Use Red + Yellow + Skin Tones
- **Sci-Fi**: Use Cyan + Light Blue + Purple
- **Spooky**: Use White + Black + Yellow
- **Grass/Nature**: Use Green + Light Green + Brown

---

## Common Mistakes

❌ **Can't paint anything?** - Make sure you've selected a color (not black)

❌ **Animation too fast?** - Increase the speed value (200-300ms)

❌ **Animation too slow?** - Decrease the speed value (50-100ms)

❌ **Made a mistake?** - Click "Clear" to start the tile over

---

## Keyboard Shortcuts Coming Soon! 🚀

The next version will include:
- **Ctrl+Z** = Undo
- **Ctrl+C** = Copy tile
- **Ctrl+V** = Paste tile
- **F** = Flip tile horizontally
- **R** = Rotate tile 90°

---

## Need Help?

Check the full README.md for detailed documentation about all features!

---

**Have fun creating retro C64 animations!** 🎮✨
