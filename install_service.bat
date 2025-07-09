@echo off
echo Installing HTML to DOCX Converter Service...

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.7+ and try again
    pause
    exit /b 1
)

REM Install required packages
echo Installing required packages...
pip install -r requirements.txt

REM Install the service
echo Installing Windows service...
python html_to_docx_converter.py install

REM Start the service
echo Starting the service...
python html_to_docx_converter.py start

echo.
echo Service installation completed!
echo The HTML to DOCX Converter Service is now running in the background.
echo It will automatically convert any HTML files downloaded to your Downloads folder.
echo.
echo To manage the service, use these commands:
echo   - Stop service: python html_to_docx_converter.py stop
echo   - Start service: python html_to_docx_converter.py start
echo   - Remove service: python html_to_docx_converter.py remove
echo.
echo Logs are stored in: C:\ProgramData\HTMLConverter\logs\html_converter.log
echo.
pause 