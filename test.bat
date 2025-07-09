@echo off
echo HTML to DOCX Converter - Test Mode
echo ==================================
echo.

set "INSTALL_DIR=C:\Program Files\HTMLtoDOCXConverter"

if exist "%INSTALL_DIR%\HTMLtoDOCXConverter.exe" (
    echo Running test conversion...
    "%INSTALL_DIR%\HTMLtoDOCXConverter.exe" test
) else (
    echo ERROR: Converter not installed.
    echo Please run install.bat first.
)

echo.
pause
