# HTML to DOCX Converter Service

A Windows background service that automatically monitors your Downloads folder and converts HTML files to DOCX format as soon as they are downloaded.

## Features

- **Automatic Monitoring**: Watches your Downloads folder for new HTML files
- **Background Service**: Runs as a Windows service, no user interaction required
- **Format Preservation**: Converts HTML formatting to Word document structure with CSS styling support
- **Minimal Margins**: Document margins set to 0.5cm (0.2 inches) for maximum content area
- **Clean Operation**: Removes original HTML files after successful conversion
- **Comprehensive Logging**: Detailed logs stored in `C:\ProgramData\HTMLConverter\logs\`

## Supported HTML Elements

- Headings (H1-H6)
- Paragraphs
- Lists (ordered and unordered)
- Tables
- Basic text formatting
- Nested elements (div, span, section, article)

## CSS Styling Support

The converter preserves CSS styling including:

- **Font properties**: size, weight (bold), style (italic), color
- **Text alignment**: left, center, right, justify
- **Text decoration**: underline
- **Line height**: spacing between lines
- **Background colors**: for text elements
- **Inline styles**: applied directly to elements
- **Style tags**: CSS rules defined in `<style>` tags
- **Color formats**: Hex colors (#RRGGBB) converted to RGB

## Requirements

- Windows 10/11
- Python 3.7 or higher
- Administrator privileges (for service installation)

## Installation

### Quick Install (Recommended)

1. **Download the files** to a folder on your computer
2. **Right-click** on `install_service.bat` and select **"Run as administrator"**
3. The script will automatically:
   - Install required Python packages
   - Install the Windows service
   - Start the service

### Manual Installation

1. **Install Python dependencies**:

   ```cmd
   pip install -r requirements.txt
   ```

2. **Install the service** (run as administrator):

   ```cmd
   python html_to_docx_converter.py install
   ```

3. **Start the service**:
   ```cmd
   python html_to_docx_converter.py start
   ```

## Usage

Once installed, the service runs automatically in the background. Simply:

1. **Download any HTML file** to your Downloads folder
2. The service will **automatically detect** the new file
3. It will **convert it to DOCX** format
4. The **original HTML file will be removed**
5. The **DOCX file will be saved** in the same location

## Testing

To test if the converter is working:

1. Run the test script:

   ```cmd
   python test_converter.py
   ```

2. This will create a sample HTML file and convert it to DOCX

## Service Management

### Start the Service

```cmd
python html_to_docx_converter.py start
```

### Stop the Service

```cmd
python html_to_docx_converter.py stop
```

### Remove the Service

```cmd
python html_to_docx_converter.py remove
```

### Quick Uninstall

Run `uninstall_service.bat` as administrator to completely remove the service.

## Console Mode

For testing or manual operation, you can run the converter in console mode:

```cmd
python html_to_docx_converter.py
```

This will start monitoring your Downloads folder and display real-time conversion activity. Press Ctrl+C to stop.

## Logs

Service logs are stored in:

```
C:\ProgramData\HTMLConverter\logs\html_converter.log
```

Check this file if you encounter any issues or want to see conversion history.

## Troubleshooting

### Service Won't Start

1. Ensure you're running as administrator
2. Check if Python is installed and in PATH
3. Verify all dependencies are installed
4. Check the Windows Event Viewer for service errors

### Conversion Fails

1. Check the log file for error details
2. Ensure the HTML file is not corrupted
3. Verify the Downloads folder path is accessible

### Permission Issues

1. Run all commands as administrator
2. Ensure the Downloads folder is not read-only
3. Check Windows Defender or antivirus settings

## File Structure

```
converter/
├── html_to_docx_converter.py    # Main service application
├── requirements.txt             # Python dependencies
├── install_service.bat          # Automatic installation script
├── uninstall_service.bat        # Automatic uninstallation script
├── test_converter.py            # Test script
└── README.md                    # This file
```

## Technical Details

- **File Monitoring**: Uses `watchdog` library for efficient file system monitoring
- **HTML Parsing**: Uses `BeautifulSoup` for robust HTML parsing
- **DOCX Generation**: Uses `python-docx` for Word document creation
- **Service Framework**: Uses `pywin32` for Windows service functionality
- **Logging**: Comprehensive logging with file and console output

## Security Notes

- The service runs with system privileges
- It only monitors the Downloads folder
- No network access or data transmission
- All processing is local to your computer

## License

This project is provided as-is for personal use. Feel free to modify and distribute as needed.
