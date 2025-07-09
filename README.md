# HTML to DOCX Converter Service

[![Build Status](https://github.com/samaritan-dev/test-docx/actions/workflows/ci.yml/badge.svg)](https://github.com/samaritan-dev/test-docx/actions/workflows/ci.yml)
[![Test Status](https://github.com/samaritan-dev/test-docx/actions/workflows/test.yml/badge.svg)](https://github.com/samaritan-dev/test-docx/actions/workflows/test.yml)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Coverage](https://codecov.io/gh/samaritan-dev/test-docx/branch/main/graph/badge.svg)](https://codecov.io/gh/samaritan-dev/test-docx)
[![Security](https://img.shields.io/badge/security-scanned-brightgreen.svg)](https://github.com/samaritan-dev/test-docx/actions/workflows/test.yml)
[![Standalone](https://img.shields.io/badge/standalone-executable-orange.svg)](README_STANDALONE.md)

A Windows background service that automatically monitors your Downloads folder and converts HTML files to DOCX format as soon as they are downloaded. Available in both Python and standalone executable versions.

## 🎯 **Two Installation Options**

### **Option 1: Standalone Executable (Recommended)**

- **No Python required** - Just click and install
- **Single executable** - Contains everything needed
- **One-click installation** - Professional installer
- **Perfect for distribution** - Share with anyone

### **Option 2: Python Version**

- **Requires Python** - For developers and advanced users
- **Customizable** - Easy to modify and extend
- **Source code access** - Full control over functionality

## ✨ **Features**

- **Automatic Monitoring**: Watches your Downloads folder for new HTML files
- **Background Service**: Runs as a Windows service, no user interaction required
- **Format Preservation**: Converts HTML formatting to Word document structure with CSS styling support
- **Minimal Margins**: Document margins set to 0.5cm (0.2 inches) for maximum content area
- **Clean Operation**: Removes original HTML files after successful conversion
- **Comprehensive Logging**: Detailed logs stored in `C:\ProgramData\HTMLConverter\logs\`
- **Automatic Startup**: Service starts automatically on Windows boot
- **CSS Styling Support**: Preserves colors, fonts, alignment, and formatting

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

## 📋 **Requirements**

### **Standalone Version:**

- Windows 10/11 (64-bit recommended)
- Administrator privileges (for installation only)
- Downloads folder (standard Windows location)

### **Python Version:**

- Windows 10/11
- Python 3.7 or higher
- Administrator privileges (for service installation)

## 🚀 **Installation**

### **Option 1: Standalone Executable (Recommended)**

#### **Quick Install:**

1. **Build the standalone executable** (one-time setup):

   ```cmd
   build_standalone.bat
   ```

2. **Copy the generated files** to any Windows system:

   - `HTMLtoDOCXConverter.exe`
   - `install_standalone.bat`
   - `uninstall_standalone.bat`
   - `test_converter.bat`

3. **Install on target system**:
   - **Right-click** `install_standalone.bat`
   - **Select "Run as administrator"**
   - **That's it!** No Python or dependencies needed

#### **What the standalone installer does:**

- ✅ Installs to `C:\Program Files\HTMLtoDOCXConverter\`
- ✅ Sets up Windows service automatically
- ✅ Configures automatic startup on boot
- ✅ Starts monitoring immediately
- ✅ No Python or dependencies required

### **Option 2: Python Version**

#### **Quick Install:**

1. **Download the files** to a folder on your computer
2. **Right-click** on `install_service.bat` and select **"Run as administrator"**
3. The script will automatically:
   - Install required Python packages
   - Install the Windows service
   - Start the service

#### **Manual Installation:**

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

## 🎯 **Usage**

Once installed, the service runs automatically in the background. Simply:

1. **Download any HTML file** to your Downloads folder
2. The service will **automatically detect** the new file
3. It will **convert it to DOCX** format with preserved styling
4. The **original HTML file will be removed**
5. The **DOCX file will be saved** in the same location

### **Automatic Startup:**

- ✅ **Service starts automatically** on Windows boot
- ✅ **No user login required** - runs in background
- ✅ **Always monitoring** Downloads folder
- ✅ **Persists across restarts** and updates

## 🧪 **Testing**

### **Standalone Version:**

1. **Right-click** `test_converter.bat`
2. **Select "Run as administrator"**
3. This will create a sample HTML file and convert it to DOCX

### **Python Version:**

1. Run the test script:

   ```cmd
   python test_converter.py
   ```

2. This will create a sample HTML file and convert it to DOCX

## 🛠️ **Service Management**

### **Standalone Version:**

#### **Start the Service:**

```cmd
"C:\Program Files\HTMLtoDOCXConverter\HTMLtoDOCXConverter.exe" start
```

#### **Stop the Service:**

```cmd
"C:\Program Files\HTMLtoDOCXConverter\HTMLtoDOCXConverter.exe" stop
```

#### **Remove the Service:**

```cmd
"C:\Program Files\HTMLtoDOCXConverter\HTMLtoDOCXConverter.exe" remove
```

#### **Quick Uninstall:**

Right-click `uninstall_standalone.bat` → "Run as administrator"

### **Python Version:**

#### **Start the Service:**

```cmd
python html_to_docx_converter.py start
```

#### **Stop the Service:**

```cmd
python html_to_docx_converter.py stop
```

#### **Remove the Service:**

```cmd
python html_to_docx_converter.py remove
```

#### **Quick Uninstall:**

Run `uninstall_service.bat` as administrator to completely remove the service.

## 🖥️ **Console Mode**

### **Python Version:**

For testing or manual operation, you can run the converter in console mode:

```cmd
python html_to_docx_converter.py
```

This will start monitoring your Downloads folder and display real-time conversion activity. Press Ctrl+C to stop.

### **Standalone Version:**

For testing the standalone executable:

```cmd
"C:\Program Files\HTMLtoDOCXConverter\HTMLtoDOCXConverter.exe" test
```

This will run a test conversion and show the results.

## 📋 **Logs**

Service logs are stored in:

```
C:\ProgramData\HTMLConverter\logs\html_converter.log
```

Check this file if you encounter any issues or want to see conversion history.

## 🔍 **Troubleshooting**

### **Service Won't Start**

#### **Standalone Version:**

1. Ensure you're running as administrator
2. Check Windows Event Viewer for service errors
3. Verify Downloads folder exists and is accessible

#### **Python Version:**

1. Ensure you're running as administrator
2. Check if Python is installed and in PATH
3. Verify all dependencies are installed
4. Check the Windows Event Viewer for service errors

### **Conversion Fails**

1. Check the log file for error details
2. Ensure the HTML file is not corrupted
3. Verify the Downloads folder path is accessible

### **Permission Issues**

1. Run all commands as administrator
2. Ensure the Downloads folder is not read-only
3. Check Windows Defender or antivirus settings

### **"Access Denied" Errors**

1. Run installer as administrator
2. Check Windows Defender settings
3. Verify Downloads folder permissions

## 📁 **File Structure**

### **Complete Project:**

```
converter/
├── html_to_docx_converter.py    # Main service application
├── requirements.txt             # Python dependencies
├── build_exe.py                 # Standalone executable builder
├── build_standalone.bat         # One-click build script
├── install_service.bat          # Python version installer
├── uninstall_service.bat        # Python version uninstaller
├── install_standalone.bat       # Standalone version installer
├── uninstall_standalone.bat     # Standalone version uninstaller
├── configure_startup.bat        # Startup configuration
├── test_converter.py            # Test script
├── README.md                    # This file
└── README_STANDALONE.md         # Standalone version documentation
```

### **After Building Standalone:**

```
dist/
├── HTMLtoDOCXConverter.exe      # Standalone executable
├── install_standalone.bat       # One-click installer
├── uninstall_standalone.bat     # Easy uninstaller
└── test_converter.bat           # Test script
```

## 🔧 **Technical Details**

### **Core Technologies:**

- **File Monitoring**: Uses `watchdog` library for efficient file system monitoring
- **HTML Parsing**: Uses `BeautifulSoup` for robust HTML parsing
- **DOCX Generation**: Uses `python-docx` for Word document creation
- **Service Framework**: Uses `pywin32` for Windows service functionality
- **Logging**: Comprehensive logging with file and console output

### **Standalone Build:**

- **PyInstaller**: Packages Python interpreter and all dependencies
- **Single Executable**: Contains everything needed to run
- **Windows Service**: Professional installation and management
- **Automatic Startup**: Configures service to start on boot

## 🔒 **Security Notes**

- **Local Only**: No network access or data transmission
- **Downloads Only**: Only monitors your Downloads folder
- **System Service**: Runs with system privileges
- **No External Dependencies**: Everything is self-contained
- **No Data Collection**: No information is sent anywhere

## 📄 **License**

This project is provided as-is for personal use. Feel free to modify and distribute as needed.

---

## 🎉 **Quick Start Summary**

### **For End Users (Standalone):**

1. Get the 4 files from the `dist/` folder
2. Right-click `install_standalone.bat` → "Run as administrator"
3. That's it! No Python or dependencies needed

### **For Developers (Python):**

1. Install Python 3.7+
2. Run `install_service.bat` as administrator
3. Service starts automatically on boot

### **For Distribution:**

1. Run `build_standalone.bat` to create executable
2. Share the 4 files from `dist/` folder
3. Anyone can install with one click

**Happy converting! 🚀**
