@echo off
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
set "INSTALL_DIR=C:\Program Files\HTMLtoDOCXConverter"
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
copy "%EXE_NAME%" "%INSTALL_DIR%\" >nul
if errorlevel 1 (
    echo ERROR: Failed to copy executable
    pause
    exit /b 1
)

REM Create log directory
set "LOG_DIR=C:\ProgramData\HTMLConverter\logs"
if not exist "%LOG_DIR%" (
    mkdir "%LOG_DIR%"
)

REM Install Windows service using sc command
echo Installing Windows service...
sc create "HTMLtoDOCXConverter" binPath= ""%INSTALL_DIR%\%EXE_NAME%"" start= auto DisplayName= "HTML to DOCX Converter Service"
if errorlevel 1 (
    echo WARNING: Service creation failed, trying alternative method...
    "%INSTALL_DIR%\%EXE_NAME%" install
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
    "%INSTALL_DIR%\%EXE_NAME%" start
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
echo - Logs: %LOG_DIR%\html_converter.log
echo.
echo To manage the service:
echo - Stop: sc stop HTMLtoDOCXConverter
echo - Start: sc start HTMLtoDOCXConverter
echo - Remove: sc delete HTMLtoDOCXConverter
echo.
pause
