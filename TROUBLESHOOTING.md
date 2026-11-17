# C64 Tile Animator - Troubleshooting Guide

## Common Issues & Solutions

---

## 🚫 Application Won't Start

### "ModuleNotFoundError: No module named 'PIL'"

**Problem**: Pillow library is not installed

**Solution**:
```bash
pip install Pillow
```

Or reinstall all requirements:
```bash
pip install -r requirements.txt
```

---

### "ModuleNotFoundError: No module named 'tkinter'"

**Problem**: Tkinter is not installed (usually on Linux)

**Solution**:

**Ubuntu/Debian**:
```bash
sudo apt-get install python3-tk
```

**Fedora/RHEL**:
```bash
sudo dnf install python3-tkinter
```

**Arch**:
```bash
sudo pacman -S tk
```

**macOS**:
Tkinter comes with Python. Try reinstalling Python from [python.org](https://www.python.org/downloads/)

---

### "Python is not recognized"

**Problem**: Python is not in your system PATH

**Solution (Windows)**:
1. Uninstall Python from Control Panel
2. Download from [python.org](https://www.python.org/downloads/)
3. Run installer
4. **CHECK "Add Python to PATH"** (important!)
5. Click Install

**Solution (macOS/Linux)**:
1. Use `python3` instead of `python`
2. Create alias in terminal: `alias python=python3`

---

### No window appears when running

**Problem**: Application runs but no window shows

**Solution**:
1. Check terminal for error messages
2. Try verbose mode:
   ```bash
   python -u c64_tile_animator.py
   ```
3. Check if running over SSH without X11 display
4. Try waiting 5-10 seconds for window to appear

**On WSL (Windows Subsystem for Linux)**:
1. Install VcXsrv: https://sourceforge.net/projects/vcxsrv/
2. Run XLaunch (use default settings)
3. Set display:
   ```bash
   export DISPLAY=localhost:0
   python3 c64_tile_animator.py
   ```

---

## 🎨 Painting Issues

### Can't paint anything / Clicking does nothing

**Problem**: No pixels appear when clicking

**Causes & Solutions**:
1. **Wrong color selected** - Black on black is invisible
   - Solution: Select a different color from the palette
   
2. **Clicking outside canvas** - Make sure you're in the grid area
   - Solution: Click in the center panel where the grid is shown
   
3. **Wrong tile size** - Verify tile size matches what you expect
   - Solution: Check tile size selection on left panel

---

### Pixels appear in wrong location

**Problem**: Paint pixels show up offset or misaligned

**Solution**:
1. Clear the tile (click "Clear" button)
2. Try again with a fresh start
3. Increase zoom level for precise control

---

### Can't erase pixels

**Problem**: Right-click doesn't erase

**Solution**:
1. Make sure you're **right-clicking and dragging** (not just clicking)
2. Try using left-click to paint over with black color
3. Use "Clear" button to clear entire tile

---

## 🎬 Animation Issues

### Animation won't play / Play button does nothing

**Problem**: Animation doesn't start when clicking Play

**Solutions**:
1. **Need at least 2 tiles** - Create a second tile first
   - Solution: Click "+ New" to add another tile
   
2. **Already playing** - Maybe it's already animating
   - Solution: Click "⏸ Stop" then click "▶ Play" again
   
3. **Preview area is off-screen** - Try resizing window
   - Solution: Drag window edge to make it larger

---

### Animation is too fast

**Problem**: Tiles change too quickly

**Solution**:
1. Drag the "Animation Speed" slider to the right
2. Higher values = slower animation
3. Try 150-200ms for natural motion

---

### Animation is too slow

**Problem**: Takes too long between frames

**Solution**:
1. Drag the "Animation Speed" slider to the left
2. Lower values = faster animation
3. Try 50-100ms for quick motion

---

### Preview window is very small or black

**Problem**: Can't see animation in preview

**Solutions**:
1. Create a tile first (should have pixels)
2. Make sure tile size is selected
3. Try playing animation
4. Check if animation is actually running (look for status)

---

## 📁 File Issues

### Can't save file / "Permission Denied"

**Problem**: Save operation fails

**Solutions**:
1. **Wrong folder** - Make sure folder is writable
   - Solution: Save to Desktop or Documents folder
   
2. **File is locked** - File might be open elsewhere
   - Solution: Close other programs using the file
   
3. **Disk full** - Not enough space
   - Solution: Free up disk space or delete old files

---

### Can't load file / "File not found"

**Problem**: Load operation fails

**Solutions**:
1. **Wrong filename** - Check the exact filename
2. **Wrong location** - File might be in different folder
3. **Wrong format** - File might not be a .c64 JSON file
4. **Corrupted file** - File might be damaged
   - Solution: Try opening with text editor to check if valid JSON

---

### File is corrupted / "JSON Decode Error"

**Problem**: Loading file causes error

**Solutions**:
1. **File is not valid JSON** - Don't manually edit .c64 files
2. **File got truncated** - Might be incomplete download
3. **Wrong format** - Make sure it's a .c64 file
4. **Backup copy** - Try loading an older backup if available

---

## 🖥️ Display Issues

### Window is too small / Controls cut off

**Problem**: Can't see all UI elements

**Solutions**:
1. **Maximize window** - Click maximize button or drag corner
2. **Resize window** - Drag window edges to make larger
3. **Higher resolution** - Change desktop resolution
4. **Smaller text** - Adjust system font size

---

### Colors look wrong / Palette not showing

**Problem**: Colors appear different or palette is hidden

**Solutions**:
1. **Scroll palette** - Use scrollbar to see all colors
2. **Wrong display** - Check monitor color settings
3. **Zoom out** - Reduce zoom level to see more palette
4. **Restart app** - Close and reopen the application

---

### Grid lines are hard to see

**Problem**: Can't see the pixel grid clearly

**Solutions**:
1. **Increase zoom** - Drag zoom slider right for bigger grid
2. **Adjust colors** - Use high contrast colors
3. **Different tile size** - Try a larger tile size (16x16 or 32x32)
4. **Monitor brightness** - Adjust monitor brightness/contrast

---

## ⚙️ Performance Issues

### Application runs slowly / Lags during painting

**Problem**: Lag when editing tiles

**Solutions**:
1. **Close other programs** - Free up system memory
2. **Reduce zoom** - Lower zoom level (less rendering)
3. **Smaller tile size** - Use 8x8 instead of 32x32
4. **Restart application** - Close and reopen
5. **Check RAM usage** - Look for other memory-intensive apps

---

### Animation preview is choppy / Stuttering

**Problem**: Animation frame rate is inconsistent

**Solutions**:
1. **Close other programs** - Running apps use CPU
2. **Increase speed value** - Slower animations run smoother
3. **Smaller preview** - Window size doesn't matter, but CPU does
4. **Lower system load** - Close web browser, etc.
5. **Update graphics drivers** - If problem persists

---

## 🔧 Specific Error Messages

### "IndexError: list index out of range"

**Problem**: Trying to access tile that doesn't exist

**Solution**:
1. Create at least one tile first (should happen automatically)
2. If error happens repeatedly, delete the app and reinstall

---

### "KeyError in pixel_data"

**Problem**: Tile data is corrupted

**Solution**:
1. Clear the tile and start over
2. Create a new project if problem persists
3. Check if you manually edited a .c64 file

---

### "TypeError: unsupported operand type(s)"

**Problem**: Code type mismatch (usually in development)

**Solution**:
1. Make sure you're using the unmodified application
2. Reinstall from scratch
3. Report issue if it persists

---

## 🆘 Still Not Working?

If none of these solutions work:

1. **Gather information**:
   - What OS are you using? (Windows/macOS/Linux)
   - What Python version? (`python --version`)
   - What's the exact error message?
   - What were you doing when it happened?

2. **Try the basics**:
   ```bash
   # Reinstall Python dependencies
   pip install -r requirements.txt --force-reinstall
   
   # Test Python installation
   python -m tkinter  # Opens a test window
   ```

3. **Clear and restart**:
   - Close the application completely
   - Wait 10 seconds
   - Reopen the application

4. **Document the issue**:
   - Take a screenshot
   - Save the error message
   - Note when it happens (startup, painting, etc.)

---

## 💡 Tips for Preventing Problems

1. **Save frequently** - Don't lose work to crashes
2. **Keep backups** - Copy .c64 files to another location
3. **Update Python** - Use latest Python 3.9+
4. **Close other apps** - Frees up system resources
5. **Restart periodically** - Prevents memory leaks
6. **Don't edit .c64 files** - Only use the application
7. **Use valid filenames** - Avoid special characters in filenames

---

## 📞 Getting More Help

- **Installation help**: See [INSTALL.md](INSTALL.md)
- **Features overview**: See [FEATURES.md](FEATURES.md)
- **Quick start**: See [QUICKSTART.md](QUICKSTART.md)
- **Full guide**: See [README.md](README.md)

---

## ✅ Verification Checklist

Before considering something broken, verify:

- [ ] Python 3.7+ is installed
- [ ] Pillow is installed (`pip list | grep Pillow`)
- [ ] tkinter works (`python -m tkinter`)
- [ ] You can open and move the window
- [ ] You can select colors
- [ ] You can click in the editor canvas
- [ ] You have at least one tile created

If all these work, the application is functioning correctly!

---

**Last Updated**: 2024
**Version**: 1.0.0
