#!/usr/bin/env python3
"""
Build script for completely standalone HTML to DOCX converter
No Python required on target systems
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def install_pyinstaller():
    """Install PyInstaller if not already installed."""
    try:
        import PyInstaller
        print("✓ PyInstaller already installed")
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✓ PyInstaller installed successfully")

def build_standalone_exe():
    """Build the standalone executable using PyInstaller."""
    is_windows = sys.platform.startswith("win")
    pathsep = ";" if is_windows else ":"
    cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name=HTMLtoDOCXConverter",
    ]
    # Windows-specific hidden imports
    if is_windows:
        cmd += [
            "--hidden-import=win32serviceutil",
            "--hidden-import=win32service",
            "--hidden-import=win32event",
            "--hidden-import=servicemanager",
            "--hidden-import=win32api",
            "--hidden-import=win32con",
            "--hidden-import=win32security",
            "--hidden-import=win32timezone",
            "--collect-all=win32",
        ]
    # Common hidden imports
    cmd += [
        "--hidden-import=watchdog.observers.winapi",
        "--hidden-import=watchdog.events",
        "--hidden-import=bs4",
        "--hidden-import=docx",
        "--hidden-import=lxml",
        "--hidden-import=psutil",
        "--collect-all=watchdog",
        "--collect-all=bs4",
        "--collect-all=docx",
        "--collect-all=lxml",
        "--collect-all=psutil",
        # Uncomment the next line if you want to include requirements.txt (optional)
        # f"--add-data=requirements.txt{pathsep}.",
        "--distpath=dist",
        "--workpath=build",
        "--specpath=build",
        "html_to_docx_converter.py"
    ]
    try:
        subprocess.check_call(cmd)
        print("✓ Standalone executable built successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Build failed: {e}")
        return False

def create_installer_script():
    """Create a pure batch installer with no Python dependencies."""
    installer_content = '''@echo off
setlocal enabledelayedexpansion

echo HTML to DOCX Converter - Standalone Installer
echo =============================================
echo.

REM Check if running as administrator
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Running as administrator - OK
) else (
    echo ERROR: This installer requires administrator privileges.
    echo Please right-click and select "Run as administrator"
    pause
    exit /b 1
)

echo.
echo Installing HTML to DOCX Converter Service...
echo.

REM Set installation directory
set "INSTALL_DIR=C:\\Program Files\\HTMLtoDOCXConverter"
set "EXE_NAME=HTMLtoDOCXConverter.exe"

REM Create installation directory
if not exist "%INSTALL_DIR%" (
    mkdir "%INSTALL_DIR%"
    if errorlevel 1 (
        echo ERROR: Failed to create installation directory
        pause
        exit /b 1
    )
)

REM Copy executable
copy "%EXE_NAME%" "%INSTALL_DIR%\\" >nul
if errorlevel 1 (
    echo ERROR: Failed to copy executable
    pause
    exit /b 1
)

REM Create log directory
set "LOG_DIR=C:\\ProgramData\\HTMLConverter\\logs"
if not exist "%LOG_DIR%" (
    mkdir "%LOG_DIR%"
)

REM Install Windows service using sc command
echo Installing Windows service...
sc create "HTMLtoDOCXConverter" binPath= "\"%INSTALL_DIR%\\%EXE_NAME%\"" start= auto DisplayName= "HTML to DOCX Converter Service"
if errorlevel 1 (
    echo WARNING: Service creation failed, trying alternative method...
    "%INSTALL_DIR%\\%EXE_NAME%" install
    if errorlevel 1 (
        echo ERROR: Failed to install service
        pause
        exit /b 1
    )
)

REM Start the service
echo Starting the service...
sc start "HTMLtoDOCXConverter"
if errorlevel 1 (
    echo WARNING: Service start failed, trying alternative method...
    "%INSTALL_DIR%\\%EXE_NAME%" start
    if errorlevel 1 (
        echo ERROR: Failed to start service
        pause
        exit /b 1
    )
)

echo.
echo =============================================
echo Installation completed successfully!
echo.
echo The HTML to DOCX Converter Service is now running.
echo It will automatically convert HTML files in your Downloads folder.
echo.
echo Service Details:
echo - Name: HTMLtoDOCXConverter
echo - Location: %INSTALL_DIR%
echo - Logs: %LOG_DIR%\\html_converter.log
echo.
echo To manage the service:
echo - Stop: sc stop HTMLtoDOCXConverter
echo - Start: sc start HTMLtoDOCXConverter
echo - Remove: sc delete HTMLtoDOCXConverter
echo.
pause
'''
    
    with open("install.bat", "w") as f:
        f.write(installer_content)
    
    print("✓ Pure batch installer created: install.bat")

def create_uninstaller_script():
    """Create a pure batch uninstaller."""
    uninstaller_content = '''@echo off
setlocal enabledelayedexpansion

echo HTML to DOCX Converter - Uninstaller
echo ====================================
echo.

REM Check if running as administrator
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Running as administrator - OK
) else (
    echo ERROR: This uninstaller requires administrator privileges.
    echo Please right-click and select "Run as administrator"
    pause
    exit /b 1
)

echo.
echo Uninstalling HTML to DOCX Converter Service...
echo.

set "INSTALL_DIR=C:\\Program Files\\HTMLtoDOCXConverter"
set "LOG_DIR=C:\\ProgramData\\HTMLConverter"

REM Stop the service
echo Stopping the service...
sc stop "HTMLtoDOCXConverter" >nul 2>&1

REM Remove the service
echo Removing the service...
sc delete "HTMLtoDOCXConverter" >nul 2>&1

REM Alternative removal method
if exist "%INSTALL_DIR%\\HTMLtoDOCXConverter.exe" (
    "%INSTALL_DIR%\\HTMLtoDOCXConverter.exe" stop >nul 2>&1
    "%INSTALL_DIR%\\HTMLtoDOCXConverter.exe" remove >nul 2>&1
)

REM Remove installation directory
if exist "%INSTALL_DIR%" (
    echo Removing installation files...
    rmdir /s /q "%INSTALL_DIR%"
)

REM Remove logs directory
if exist "%LOG_DIR%" (
    echo Removing log files...
    rmdir /s /q "%LOG_DIR%"
)

echo.
echo =============================================
echo Uninstallation completed successfully!
echo.
pause
'''
    
    with open("uninstall.bat", "w") as f:
        f.write(uninstaller_content)
    
    print("✓ Pure batch uninstaller created: uninstall.bat")

def create_test_script():
    """Create a test script that doesn't require Python."""
    test_content = '''@echo off
echo HTML to DOCX Converter - Test Mode
echo ==================================
echo.

set "INSTALL_DIR=C:\\Program Files\\HTMLtoDOCXConverter"

if exist "%INSTALL_DIR%\\HTMLtoDOCXConverter.exe" (
    echo Running test conversion...
    "%INSTALL_DIR%\\HTMLtoDOCXConverter.exe" test
) else (
    echo ERROR: Converter not installed.
    echo Please run install.bat first.
)

echo.
pause
'''
    
    with open("test.bat", "w") as f:
        f.write(test_content)
    
    print("✓ Test script created: test.bat")

def create_readme():
    """Create a simple README for the standalone version."""
    readme_content = '''# HTML to DOCX Converter - Standalone

**No Python Required!** Just click and install.

## Installation

1. **Right-click** `install.bat`
2. **Select "Run as administrator"**
3. **That's it!** The service is now running

## Testing

1. **Right-click** `test.bat`
2. **Select "Run as administrator"**
3. It will create a sample HTML file and convert it

## Uninstallation

1. **Right-click** `uninstall.bat`
2. **Select "Run as administrator"**
3. The service will be completely removed

## How It Works

- Monitors your Downloads folder for HTML files
- Automatically converts them to DOCX format
- Removes original HTML files after conversion
- Runs as a Windows service (starts automatically on boot)

## Files Included

- `HTMLtoDOCXConverter.exe` - The standalone executable
- `install.bat` - One-click installer
- `uninstall.bat` - Easy uninstaller
- `test.bat` - Test script

## Requirements

- Windows 10/11
- Administrator privileges (for installation only)

That's it! No Python, no dependencies, no drama.
'''
    
    with open("README_STANDALONE.txt", "w") as f:
        f.write(readme_content)
    
    print("✓ Standalone README created: README_STANDALONE.txt")

def main():
    """Main build process."""
    print("HTML to DOCX Converter - Standalone Build")
    print("=" * 40)
    print()
    
    # Install PyInstaller
    install_pyinstaller()
    print()
    
    # Build executable
    if build_standalone_exe():
        print()
        # Create installer scripts
        create_installer_script()
        create_uninstaller_script()
        create_test_script()
        create_readme()
        
        print()
        print("=" * 40)
        print("BUILD COMPLETED SUCCESSFULLY!")
        print("=" * 40)
        print()
        print("Files created:")
        print("- dist/HTMLtoDOCXConverter.exe (standalone executable)")
        print("- install.bat (pure batch installer)")
        print("- uninstall.bat (pure batch uninstaller)")
        print("- test.bat (test script)")
        print("- README_STANDALONE.txt (instructions)")
        print()
        print("To distribute:")
        print("1. Copy all files from dist/ folder")
        print("2. Share with anyone")
        print("3. They just run install.bat as administrator")
        print("4. No Python or dependencies needed!")
        print()
    else:
        print("Build failed. Please check the error messages above.")

if __name__ == "__main__":
    main() 