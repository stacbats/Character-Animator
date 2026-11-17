# C64 Tile Animator - Installation Guide

## System Requirements

- **Python**: 3.7 or higher
- **OS**: Windows, macOS, or Linux
- **RAM**: 512 MB minimum
- **Disk Space**: 50 MB (including Python libraries)

---

## Installation by Platform

### Windows

#### Option 1: Using Command Prompt (Recommended)

1. **Open Command Prompt**
   - Press `Win + R`
   - Type `cmd` and press Enter

2. **Navigate to the project folder**
   ```bash
   cd C:\path\to\C64_VSCODE\Tile_Animator
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python c64_tile_animator.py
   ```

#### Option 2: Using Windows Batch File

Create a file called `run.bat` in the project folder with this content:
```batch
@echo off
cd /d "%~dp0"
pip install -r requirements.txt
python c64_tile_animator.py
pause
```

Then double-click `run.bat` to run the application.

#### Option 3: Using PowerShell

1. Open PowerShell
2. Navigate to project folder:
   ```powershell
   cd "C:\path\to\C64_VSCODE\Tile_Animator"
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
4. Run the application:
   ```powershell
   python c64_tile_animator.py
   ```

---

### macOS

1. **Open Terminal**
   - Press `Cmd + Space`
   - Type `Terminal` and press Enter

2. **Navigate to the project folder**
   ```bash
   cd ~/path/to/C64_VSCODE/Tile_Animator
   ```

3. **Ensure Python 3 is installed**
   ```bash
   python3 --version
   ```
   If not installed, download from [python.org](https://www.python.org/downloads/)

4. **Install dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python3 c64_tile_animator.py
   ```

**Optional: Create a launcher script**

Create a file called `run.sh` with this content:
```bash
#!/bin/bash
cd "$(dirname "$0")"
pip3 install -r requirements.txt
python3 c64_tile_animator.py
```

Then make it executable and run it:
```bash
chmod +x run.sh
./run.sh
```

---

### Linux

1. **Open Terminal**
   - Usually `Ctrl + Alt + T` or find Terminal in applications

2. **Navigate to the project folder**
   ```bash
   cd ~/path/to/C64_VSCODE/Tile_Animator
   ```

3. **Ensure Python 3 is installed**
   ```bash
   python3 --version
   ```
   
   If not installed, use your package manager:
   - **Ubuntu/Debian**: `sudo apt-get install python3 python3-pip`
   - **Fedora/RHEL**: `sudo dnf install python3 python3-pip`
   - **Arch**: `sudo pacman -S python python-pip`

4. **Install dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python3 c64_tile_animator.py
   ```

**Optional: Create a launcher script**

Create a file called `run.sh`:
```bash
#!/bin/bash
cd "$(dirname "$0")"
pip3 install -r requirements.txt
python3 c64_tile_animator.py
```

Make it executable:
```bash
chmod +x run.sh
./run.sh
```

---

## Troubleshooting Installation

### "Python is not recognized"

**Windows:**
- Ensure Python is installed: [python.org](https://www.python.org/downloads/)
- Check "Add Python to PATH" during installation
- Restart Command Prompt after installation

**macOS/Linux:**
- Use `python3` instead of `python`
- Or create an alias: `alias python=python3`

### "pip: command not found"

```bash
# Windows
python -m pip install -r requirements.txt

# macOS/Linux
python3 -m pip install -r requirements.txt
```

### "ModuleNotFoundError: No module named 'PIL'"

The Pillow library isn't installed. Run:
```bash
# Windows
pip install Pillow

# macOS/Linux
pip3 install Pillow
```

### "Module 'tkinter' not found"

Tkinter should come with Python, but on some Linux systems it needs manual installation:

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-tk
```

**Fedora/RHEL:**
```bash
sudo dnf install python3-tkinter
```

**Arch:**
```bash
sudo pacman -S tk
```

### Application window won't open

- Make sure you're running it from the correct directory
- Check that all files are in place (especially `c64_tile_animator.py`)
- Try running with verbose output:
  ```bash
  python -u c64_tile_animator.py
  ```

### Tkinter display issues

If you're running over SSH or have display issues:
1. Try setting the display variable (Linux):
   ```bash
   export DISPLAY=:0
   python3 c64_tile_animator.py
   ```

2. For WSL (Windows Subsystem for Linux):
   - Install an X11 server like VcXsrv
   - Set up your display: `export DISPLAY=localhost:0`

---

## Verifying Installation

To verify everything is installed correctly:

```bash
python -c "import tkinter; print('✓ Tkinter OK')"
python -c "import PIL; print('✓ Pillow OK')"
python -c "import json; print('✓ JSON OK')"
```

All three should show checkmarks.

---

## Virtual Environment Setup (Optional but Recommended)

Using a virtual environment keeps your Python projects isolated.

### Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python c64_tile_animator.py
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 c64_tile_animator.py
```

To deactivate the virtual environment later:
```bash
deactivate
```

---

## Running from IDE

### Visual Studio Code

1. **Open project folder in VS Code**
2. **Install Python extension** (if not already installed)
3. **Open terminal** (Ctrl+`)
4. **Run**:
   ```bash
   pip install -r requirements.txt
   python c64_tile_animator.py
   ```

### PyCharm

1. **Open project**
2. **Install dependencies** via PyCharm's Package Manager
3. **Right-click** `c64_tile_animator.py`
4. **Select "Run"**

### Thonny

1. **Open** `c64_tile_animator.py`
2. **Press F5** to run
3. When prompted, install Pillow through the Tools menu

---

## Updating

To get the latest version of dependencies:

```bash
pip install -r requirements.txt --upgrade
```

---

## Uninstallation

To completely remove (keeping your project files):

```bash
# Just remove Python packages
pip uninstall Pillow -y
```

The project files and your saved .c64 files will remain intact.

---

## Getting Help

If you encounter issues:

1. **Check the QUICKSTART.md** for basic usage
2. **Review the README.md** for feature descriptions
3. **Check FEATURES.md** for detailed capabilities
4. **Verify Python version**: `python --version` (should be 3.7+)
5. **Check dependencies**: Run the verification commands above

---

**Happy animating!** 🎮✨
