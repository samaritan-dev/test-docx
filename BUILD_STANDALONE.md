# Building Standalone HTML to DOCX Converter

This guide shows how to build a completely standalone executable that requires **NO Python** on target systems.

## 🎯 **What You Get**

A single executable file that contains everything needed:

- ✅ **No Python installation** required on target systems
- ✅ **No dependencies** to install
- ✅ **Pure batch installers** (no Python scripts)
- ✅ **Self-contained** - everything packaged inside

## 🚀 **Quick Build**

### **Step 1: Build the Executable**

```cmd
build_standalone.bat
```

### **Step 2: Package for Distribution**

```cmd
package.bat
```

### **Step 3: Share the ZIP File**

The ZIP file contains everything needed for installation on any Windows system.

## 📁 **Files Created**

After building, you'll get:

### **In `dist/` folder:**

- `HTMLtoDOCXConverter.exe` - Standalone executable (contains Python + all libraries)
- `install.bat` - Pure batch installer (no Python required)
- `uninstall.bat` - Pure batch uninstaller
- `test.bat` - Test script
- `README_STANDALONE.txt` - Instructions

### **After packaging:**

- `HTMLtoDOCXConverter_Standalone_YYYYMMDD_HHMMSS.zip` - Ready to distribute

## 🔧 **How It Works**

### **PyInstaller Magic:**

- **Packages Python interpreter** inside the executable
- **Includes all libraries** (watchdog, python-docx, beautifulsoup4, etc.)
- **Single file** - everything self-contained
- **Windows service** - professional installation

### **Pure Batch Scripts:**

- **No Python commands** in installers
- **Uses Windows commands** (sc, net, etc.)
- **Works on any Windows system**
- **No dependencies** whatsoever

## 📋 **Requirements for Building**

### **On Your Development Machine:**

- Python 3.7+ (only for building)
- PyInstaller (installed automatically)
- Windows 10/11 (for Windows-specific features)

### **On Target Systems:**

- **Nothing!** No Python, no dependencies, no requirements

## 🎯 **Installation on Target Systems**

### **Step 1: Extract ZIP File**

Extract the ZIP file to any folder on the target system.

### **Step 2: Install**

1. **Right-click** `install.bat`
2. **Select "Run as administrator"**
3. **That's it!** Service is now running

### **Step 3: Test**

1. **Right-click** `test.bat`
2. **Select "Run as administrator"**
3. It will create a sample HTML file and convert it

## 🛠️ **Service Management**

### **Using Windows Commands:**

```cmd
# Stop service
sc stop HTMLtoDOCXConverter

# Start service
sc start HTMLtoDOCXConverter

# Remove service
sc delete HTMLtoDOCXConverter
```

### **Using Batch Files:**

- **Uninstall:** Right-click `uninstall.bat` → "Run as administrator"

## 🔍 **Troubleshooting**

### **Build Issues:**

- Ensure Python is installed and in PATH
- Run as administrator if needed
- Check antivirus isn't blocking PyInstaller

### **Installation Issues:**

- Run installer as administrator
- Check Windows Defender settings
- Verify Downloads folder exists

### **Service Issues:**

- Check Windows Event Viewer
- Verify service is installed: `sc query HTMLtoDOCXConverter`

## 💡 **Pro Tips**

1. **Test the build** before distributing
2. **Keep the ZIP file** for easy reinstallation
3. **Document the process** for your team
4. **Version your builds** with timestamps

## 🎉 **Distribution**

### **Share the ZIP file:**

- Email to colleagues
- Upload to file sharing
- Include in software packages
- Deploy via IT management tools

### **No Installation Complexity:**

- Recipients just extract and run
- No technical knowledge required
- Works on any Windows 10/11 system
- Professional installation experience

---

**That's it!** You now have a completely standalone solution that requires zero Python knowledge or installation on target systems! 🚀
