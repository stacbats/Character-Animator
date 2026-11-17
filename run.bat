@echo off
REM C64 Tile Animator - Quick Start for Windows
REM This batch file installs dependencies and runs the application

title C64 Tile Animator - Starting...
color 0E

echo.
echo ========================================
echo C64 Tile Animator - Quick Start
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo Checking dependencies...
pip show Pillow >nul 2>&1
if errorlevel 1 (
    echo Installing Pillow...
    pip install Pillow
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
) else (
    echo Pillow is already installed
)

echo.
echo Starting C64 Tile Animator...
echo.

REM Run the application
python c64_tile_animator.py

REM If it reaches here, app closed normally
echo.
echo Application closed.
pause
