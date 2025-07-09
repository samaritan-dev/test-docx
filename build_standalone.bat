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
python build_standalone.py

echo.
echo Build process completed!
echo.
echo Files created in dist/ folder:
echo - HTMLtoDOCXConverter.exe (standalone executable)
echo - install.bat (pure batch installer)
echo - uninstall.bat (pure batch uninstaller)
echo - test.bat (test script)
echo - README_STANDALONE.txt (instructions)
echo.
echo These files can be distributed to ANY Windows system
echo without requiring Python or any dependencies!
echo.
pause 