#!/usr/bin/env python3
"""
Build script to create a standalone executable for the HTML to DOCX converter
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

def build_executable():
    """Build the standalone executable."""
    print("Building standalone executable...")
    
    # PyInstaller command with all necessary options
    cmd = [
        "pyinstaller",
        "--onefile",                    # Single executable file
        "--windowed",                   # No console window
        "--name=HTMLtoDOCXConverter",   # Executable name
        "--add-data=requirements.txt;.", # Include requirements
        "--hidden-import=win32serviceutil",
        "--hidden-import=win32service",
        "--hidden-import=win32event",
        "--hidden-import=servicemanager",
        "--hidden-import=watchdog.observers.winapi",
        "--hidden-import=watchdog.events",
        "--hidden-import=bs4",
        "--hidden-import=docx",
        "--hidden-import=lxml",
        "--hidden-import=psutil",
        "--icon=icon.ico",              # Add icon if available
        "html_to_docx_converter.py"
    ]
    
    try:
        subprocess.check_call(cmd)
        print("✓ Executable built successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Build failed: {e}")
        return False

def create_installer():
    """Create a simple installer script."""
    installer_content = '''@echo off
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

REM Copy executable to Program Files
set "INSTALL_DIR=C:\\Program Files\\HTMLtoDOCXConverter"
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

copy "HTMLtoDOCXConverter.exe" "%INSTALL_DIR%\\" >nul
if errorlevel 1 (
    echo ERROR: Failed to copy executable
    pause
    exit /b 1
)

REM Install and start the service
cd /d "%INSTALL_DIR%"
HTMLtoDOCXConverter.exe install
if errorlevel 1 (
    echo ERROR: Failed to install service
    pause
    exit /b 1
)

REM Configure for automatic startup
sc config HTMLtoDOCXConverter start= auto
if errorlevel 1 (
    echo WARNING: Failed to configure automatic startup
)

HTMLtoDOCXConverter.exe start
if errorlevel 1 (
    echo ERROR: Failed to start service
    pause
    exit /b 1
)

echo.
echo =============================================
echo Installation completed successfully!
echo.
echo The HTML to DOCX Converter Service is now running.
echo It will automatically convert HTML files in your Downloads folder.
echo.
echo To manage the service:
echo - Stop: "%INSTALL_DIR%\\HTMLtoDOCXConverter.exe" stop
echo - Start: "%INSTALL_DIR%\\HTMLtoDOCXConverter.exe" start
echo - Remove: "%INSTALL_DIR%\\HTMLtoDOCXConverter.exe" remove
echo.
echo Logs: C:\\ProgramData\\HTMLConverter\\logs\\html_converter.log
echo.
pause
'''
    
    with open("install_standalone.bat", "w") as f:
        f.write(installer_content)
    
    print("✓ Standalone installer created: install_standalone.bat")

def create_uninstaller():
    """Create an uninstaller script."""
    uninstaller_content = '''@echo off
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

REM Stop and remove the service
if exist "%INSTALL_DIR%\\HTMLtoDOCXConverter.exe" (
    cd /d "%INSTALL_DIR%"
    HTMLtoDOCXConverter.exe stop
    HTMLtoDOCXConverter.exe remove
)

REM Remove installation directory
if exist "%INSTALL_DIR%" (
    rmdir /s /q "%INSTALL_DIR%"
)

REM Remove logs directory
if exist "C:\\ProgramData\\HTMLConverter" (
    rmdir /s /q "C:\\ProgramData\\HTMLConverter"
)

echo.
echo =============================================
echo Uninstallation completed successfully!
echo.
pause
'''
    
    with open("uninstall_standalone.bat", "w") as f:
        f.write(uninstaller_content)
    
    print("✓ Standalone uninstaller created: uninstall_standalone.bat")

def create_test_exe():
    """Create a test executable."""
    test_exe_content = '''@echo off
echo HTML to DOCX Converter - Test Mode
echo ==================================
echo.

echo This will test the converter by creating a sample HTML file
echo and converting it to DOCX format.
echo.

set "INSTALL_DIR=C:\\Program Files\\HTMLtoDOCXConverter"
if exist "%INSTALL_DIR%\\HTMLtoDOCXConverter.exe" (
    cd /d "%INSTALL_DIR%"
    echo Running test...
    HTMLtoDOCXConverter.exe test
) else (
    echo ERROR: Converter not installed. Please run install_standalone.bat first.
)

echo.
pause
'''
    
    with open("test_converter.bat", "w") as f:
        f.write(test_exe_content)
    
    print("✓ Test script created: test_converter.bat")

def main():
    """Main build process."""
    print("HTML to DOCX Converter - Standalone Build")
    print("=" * 40)
    print()
    
    # Install PyInstaller
    install_pyinstaller()
    print()
    
    # Build executable
    if build_executable():
        print()
        # Create installer scripts
        create_installer()
        create_uninstaller()
        create_test_exe()
        
        print()
        print("=" * 40)
        print("BUILD COMPLETED SUCCESSFULLY!")
        print("=" * 40)
        print()
        print("Files created:")
        print("- dist/HTMLtoDOCXConverter.exe (standalone executable)")
        print("- install_standalone.bat (one-click installer)")
        print("- uninstall_standalone.bat (uninstaller)")
        print("- test_converter.bat (test script)")
        print()
        print("To install on any Windows system:")
        print("1. Copy all files to the target system")
        print("2. Right-click install_standalone.bat → Run as administrator")
        print("3. That's it! No Python or dependencies needed.")
        print()
    else:
        print("Build failed. Please check the error messages above.")

if __name__ == "__main__":
    main() 