@echo off
echo HTML to DOCX Converter - Startup Configuration
echo ===============================================
echo.

REM Check if running as administrator
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Running as administrator - OK
) else (
    echo ERROR: This script requires administrator privileges.
    echo Please right-click and select "Run as administrator"
    pause
    exit /b 1
)

echo.
echo Checking service status...
echo.

REM Check if service exists
sc query HTMLtoDOCXConverter >nul 2>&1
if errorlevel 1 (
    echo ERROR: HTMLtoDOCXConverter service not found.
    echo Please install the service first using install_standalone.bat
    pause
    exit /b 1
)

REM Get current service status
for /f "tokens=3" %%i in ('sc query HTMLtoDOCXConverter ^| find "START_TYPE"') do set START_TYPE=%%i
for /f "tokens=3" %%i in ('sc query HTMLtoDOCXConverter ^| find "STATE"') do set STATE=%%i

echo Current Service Status:
echo - Startup Type: %START_TYPE%
echo - State: %STATE%
echo.

REM Configure startup type
echo Configuring service for automatic startup...
sc config HTMLtoDOCXConverter start= auto
if errorlevel 1 (
    echo ERROR: Failed to configure startup type
    pause
    exit /b 1
)

REM Start the service if not running
if "%STATE%"=="1" (
    echo Starting the service...
    sc start HTMLtoDOCXConverter
    if errorlevel 1 (
        echo ERROR: Failed to start service
        pause
        exit /b 1
    )
)

echo.
echo ===============================================
echo Startup configuration completed successfully!
echo.
echo The HTML to DOCX Converter Service will now:
echo - Start automatically when Windows boots
echo - Run in the background without user login
echo - Monitor your Downloads folder continuously
echo - Convert HTML files to DOCX automatically
echo.
echo Service Status:
sc query HTMLtoDOCXConverter | find "START_TYPE"
sc query HTMLtoDOCXConverter | find "STATE"
echo.
echo To verify it's working:
echo 1. Restart your computer
echo 2. Download any HTML file to Downloads folder
echo 3. It should automatically convert to DOCX
echo.
pause 