# HTML to DOCX Converter Service

[![Build Status](https://github.com/samaritan-dev/test-docx/actions/workflows/ci.yml/badge.svg)](https://github.com/samaritan-dev/test-docx/actions/workflows/ci.yml)
[![Test Status](https://github.com/samaritan-dev/test-docx/actions/workflows/test.yml/badge.svg)](https://github.com/samaritan-dev/test-docx/actions/workflows/test.yml)
[![Extensive UI Tests](https://github.com/samaritan-dev/test-docx/actions/workflows/extensive-ui-tests.yml/badge.svg)](https://github.com/samaritan-dev/test-docx/actions/workflows/extensive-ui-tests.yml)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Coverage](https://codecov.io/gh/samaritan-dev/test-docx/branch/main/graph/badge.svg)](https://codecov.io/gh/samaritan-dev/test-docx)
[![Security](https://img.shields.io/badge/security-scanned-brightgreen.svg)](https://github.com/samaritan-dev/test-docx/actions/workflows/test.yml)
[![Standalone](https://img.shields.io/badge/standalone-executable-orange.svg)](README_STANDALONE.md)
[![Accessibility](https://img.shields.io/badge/accessibility-WCAG%202.1-compliant-brightgreen.svg)](tests/test_accessibility.py)
[![Cross Browser](https://img.shields.io/badge/cross--browser-Chrome%2CFirefox%2CEdge-blue.svg)](tests/test_ui_extensive.py)

A Windows background service that automatically monitors your Downloads folder and converts HTML files to DOCX format as soon as they are downloaded. Available in both Python and standalone executable versions with comprehensive testing suite.

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
- **Comprehensive testing** - Extensive UI and accessibility testing

## ✨ **Features**

- **Automatic Monitoring**: Watches your Downloads folder for new HTML files
- **Background Service**: Runs as a Windows service, no user interaction required
- **Format Preservation**: Converts HTML formatting to Word document structure with CSS styling support
- **Minimal Margins**: Document margins set to 0.5cm (0.2 inches) for maximum content area
- **Clean Operation**: Removes original HTML files after successful conversion
- **Comprehensive Logging**: Detailed logs stored in `C:\ProgramData\HTMLConverter\logs\`
- **Automatic Startup**: Service starts automatically on Windows boot
- **CSS Styling Support**: Preserves colors, fonts, alignment, and formatting
- **Extensive Testing**: Multi-browser UI testing, accessibility compliance, and performance validation
- **Cross-Browser Compatibility**: Tested on Chrome, Firefox, and Edge
- **Responsive Design Support**: Handles various screen sizes and layouts

## 🧪 **Comprehensive Testing Suite**

### **Extensive UI Testing**

- **Multi-browser testing** (Chrome, Firefox, Edge)
- **Responsive design validation** across different viewports
- **Accessibility compliance testing** using axe-core
- **Performance benchmarking** and memory profiling
- **Cross-browser compatibility** verification
- **Comprehensive HTML/CSS rendering** validation

### **Test Categories**

1. **Basic UI Elements** - HTML structure and formatting
2. **Complex CSS Styling** - Modern CSS features and layouts
3. **Responsive Design** - Multi-viewport testing (Desktop, Tablet, Mobile)
4. **Typography & Text Effects** - Font styling and effects
5. **Tables & Forms** - Complex data structures
6. **Accessibility Testing** - WCAG 2.1 compliance
7. **Performance Testing** - Memory and speed profiling
8. **Cross-Browser Compatibility** - Chrome, Firefox, Edge

### **Testing Environments**

- **3 Python versions** (3.9, 3.10, 3.11)
- **3 browsers** (Chrome, Firefox, Edge)
- **4 viewports** (1920x1080, 1366x768, 768x1024, 375x667)
- **Parallel execution** support
- **Headless testing** for CI/CD compatibility

## Supported HTML Elements

- Headings (H1-H6)
- Paragraphs
- Lists (ordered and unordered)
- Tables
- Basic text formatting
- Nested elements (div, span, section, article)
- Forms and form elements
- Images with alt text
- Blockquotes and preformatted text

## CSS Styling Support

The converter preserves CSS styling including:

- **Font properties**: size, weight (bold), style (italic), color
- **Text alignment**: left, center, right, justify
- **Text decoration**: underline, line-through
- **Line height**: spacing between lines
- **Background colors**: for text elements
- **Inline styles**: applied directly to elements
- **Style tags**: CSS rules defined in `<style>` tags
- **Color formats**: Hex colors (#RRGGBB) converted to RGB
- **Gradient backgrounds**: Linear and radial gradients
- **Box shadows**: Drop shadows and border effects
- **CSS Grid and Flexbox**: Layout structures
- **Media queries**: Responsive design elements

## 📋 **Requirements**

### **Standalone Version:**

- Windows 10/11 (64-bit recommended)
- Administrator privileges (for installation only)
- Downloads folder (standard Windows location)

### **Python Version:**

- Windows 10/11
- Python 3.9 or higher
- Administrator privileges (for service installation)

### **Testing Requirements:**

- Python 3.9+ for running tests
- Chrome, Firefox, or Edge browsers
- Selenium WebDriver (automatically managed)
- pytest and testing dependencies

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

## 🧪 **Testing**

### **Running Tests**

#### **Option 1: Using Test Runner Script**

```bash
# Run all tests
python run_extensive_ui_tests.py

# Run specific test types
python run_extensive_ui_tests.py --test-type basic --browsers chrome
python run_extensive_ui_tests.py --test-type accessibility
python run_extensive_ui_tests.py --test-type performance --parallel

# Run with specific browsers
python run_extensive_ui_tests.py --browsers chrome,firefox,edge

# Custom output file
python run_extensive_ui_tests.py --output my-results.json
```

#### **Option 2: Using Windows Batch Script**

```cmd
# Run all tests
run_extensive_ui_tests.bat

# Run specific test types
run_extensive_ui_tests.bat --test-type basic --browsers chrome

# Run in parallel
run_extensive_ui_tests.bat --parallel
```

#### **Option 3: Using pytest directly**

```bash
# Run all UI tests
pytest tests/test_ui_extensive.py -v

# Run specific test
pytest tests/test_ui_extensive.py::TestExtensiveUI::test_basic_html_elements -v

# Run with specific browser
pytest tests/test_ui_extensive.py --browser=chrome -v

# Run accessibility tests
pytest tests/test_accessibility.py -v

# Generate HTML report
pytest tests/test_ui_extensive.py --html=reports/my-report.html --self-contained-html
```

### **Test Reports**

The testing suite generates comprehensive reports:

- **HTML reports** with screenshots and detailed results
- **JSON results** for programmatic analysis
- **GitHub Actions artifacts** for easy access
- **Performance metrics** and memory profiling
- **Accessibility compliance** reports

### **GitHub Actions Integration**

Tests automatically run on:

- Every push to `main` or `develop` branches
- Every pull request
- Manual workflow dispatch with test type selection

### **Standalone Version Testing:**

1. **Right-click** `test_converter.bat`
2. **Select "Run as administrator"**
3. This will create a sample HTML file and convert it to DOCX

### **Python Version Testing:**

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

### **Testing Issues**

1. **Browser Driver Issues**:

   ```bash
   pip install webdriver-manager --upgrade
   ```

2. **Memory Issues**:

   ```bash
   python run_extensive_ui_tests.py --parallel --max-workers 2
   ```

3. **Permission Issues**:
   ```bash
   chmod +x run_extensive_ui_tests.py  # Linux/macOS
   ```

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
├── run_extensive_ui_tests.py    # Extensive UI test runner
├── run_extensive_ui_tests.bat   # Windows test runner
├── pytest.ini                   # Pytest configuration
├── tests/                       # Test suite
│   ├── test_ui_extensive.py     # Comprehensive UI tests
│   ├── test_accessibility.py    # Accessibility tests
│   └── test_converter.py        # Unit tests
├── .github/workflows/           # GitHub Actions
│   ├── ci.yml                   # Continuous integration
│   ├── test.yml                 # Unit and integration tests
│   └── extensive-ui-tests.yml   # Extensive UI testing
├── README.md                    # This file
├── README_STANDALONE.md         # Standalone version documentation
├── EXTENSIVE_UI_TESTING.md      # Comprehensive testing documentation
└── BUILD_STANDALONE.md          # Standalone build documentation
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

### **Testing Technologies:**

- **Selenium WebDriver**: Browser automation for UI testing
- **pytest**: Testing framework with extensive plugin support
- **axe-selenium-python**: Accessibility testing with axe-core
- **webdriver-manager**: Automatic browser driver management
- **pytest-html**: HTML test reporting
- **pytest-xdist**: Parallel test execution

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
- **Input Validation**: Sanitizes HTML input to prevent XSS
- **Path Validation**: Prevents path traversal attacks

## 📊 **Quality Assurance**

### **Testing Coverage**

- **Unit Tests**: Core functionality testing
- **Integration Tests**: End-to-end workflow testing
- **UI Tests**: Browser-based rendering validation
- **Accessibility Tests**: WCAG 2.1 compliance
- **Performance Tests**: Memory and speed profiling
- **Cross-Browser Tests**: Chrome, Firefox, Edge compatibility
- **Security Tests**: Input validation and sanitization

### **Continuous Integration**

- **Automated Testing**: Runs on every commit and pull request
- **Multi-Environment**: Tests across Python versions and browsers
- **Parallel Execution**: Fast test execution with parallel processing
- **Comprehensive Reporting**: Detailed test results and artifacts
- **Quality Gates**: Prevents merging with failing tests

## 📄 **License**

This project is provided as-is for personal use. Feel free to modify and distribute as needed.

## 📚 **Documentation**

- **[README.md](README.md)** - Main documentation (this file)
- **[README_STANDALONE.md](README_STANDALONE.md)** - Standalone version guide
- **[EXTENSIVE_UI_TESTING.md](EXTENSIVE_UI_TESTING.md)** - Comprehensive testing documentation
- **[BUILD_STANDALONE.md](BUILD_STANDALONE.md)** - Standalone build guide

---

## 🎉 **Quick Start Summary**

### **For End Users (Standalone):**

1. Get the 4 files from the `dist/` folder
2. Right-click `install_standalone.bat` → "Run as administrator"
3. That's it! No Python or dependencies needed

### **For Developers (Python):**

1. Install Python 3.9+
2. Run `install_service.bat` as administrator
3. Service starts automatically on boot

### **For Testing:**

1. Install dependencies: `pip install -r requirements.txt`
2. Run tests: `python run_extensive_ui_tests.py`
3. View reports in `reports/` directory

### **For Distribution:**

1. Run `build_standalone.bat` to create executable
2. Share the 4 files from `dist/` folder
3. Anyone can install with one click

**Happy converting! 🚀**
