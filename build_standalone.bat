@echo off
echo Building Standalone HTML to DOCX Converter...
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7+ and try again
    pause
    exit /b 1
)

echo Python found. Building standalone executable...
echo.

REM Run the build script
python build_exe.py

echo.
echo Build process completed!
echo.
pause 