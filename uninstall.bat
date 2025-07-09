@echo off
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

set "INSTALL_DIR=C:\Program Files\HTMLtoDOCXConverter"
set "LOG_DIR=C:\ProgramData\HTMLConverter"

REM Stop the service
echo Stopping the service...
sc stop "HTMLtoDOCXConverter" >nul 2>&1

REM Remove the service
echo Removing the service...
sc delete "HTMLtoDOCXConverter" >nul 2>&1

REM Alternative removal method
if exist "%INSTALL_DIR%\HTMLtoDOCXConverter.exe" (
    "%INSTALL_DIR%\HTMLtoDOCXConverter.exe" stop >nul 2>&1
    "%INSTALL_DIR%\HTMLtoDOCXConverter.exe" remove >nul 2>&1
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
