@echo off
echo Uninstalling HTML to DOCX Converter Service...

REM Stop the service
echo Stopping the service...
python html_to_docx_converter.py stop

REM Remove the service
echo Removing the service...
python html_to_docx_converter.py remove

echo.
echo Service uninstallation completed!
echo The HTML to DOCX Converter Service has been removed from your system.
echo.
pause 