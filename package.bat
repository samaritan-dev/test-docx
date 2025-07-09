@echo off
echo Packaging Standalone Distribution...
echo ====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7+ and try again
    pause
    exit /b 1
)

echo Python found. Packaging distribution...
echo.

REM Run the packaging script
python package_distribution.py

echo.
echo Packaging completed!
echo.
pause 