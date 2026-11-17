#!/bin/bash
# C64 Tile Animator - Quick Start for Linux/macOS
# This script installs dependencies and runs the application

echo "========================================"
echo "C64 Tile Animator - Quick Start"
echo "========================================"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo ""
    echo "Install Python 3:"
    echo "  Ubuntu/Debian: sudo apt-get install python3 python3-pip"
    echo "  Fedora/RHEL:   sudo dnf install python3 python3-pip"
    echo "  Arch:          sudo pacman -S python python-pip"
    echo "  macOS:         brew install python3"
    echo ""
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "Python version: $PYTHON_VERSION"

# Check if tkinter is available
if ! python3 -c "import tkinter" 2>/dev/null; then
    echo "WARNING: tkinter not found"
    echo ""
    echo "Install tkinter:"
    echo "  Ubuntu/Debian: sudo apt-get install python3-tk"
    echo "  Fedora/RHEL:   sudo dnf install python3-tkinter"
    echo "  Arch:          sudo pacman -S tk"
    echo ""
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Check dependencies
echo "Checking dependencies..."
if python3 -c "import PIL" 2>/dev/null; then
    echo "Pillow is already installed"
else
    echo "Installing Pillow..."
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to install dependencies"
        exit 1
    fi
fi

echo ""
echo "Starting C64 Tile Animator..."
echo ""

# Run the application
python3 c64_tile_animator.py

# If it reaches here, app closed normally
echo ""
echo "Application closed."
