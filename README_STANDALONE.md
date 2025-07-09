# HTML to DOCX Converter - Standalone Version

**No Python Required!** Just click and install.

## 🎯 **What You Get**

A single executable file that contains everything needed to run the HTML to DOCX converter service. No Python installation, no dependencies, no complicated setup.

## 📦 **Files Included**

After building, you'll get:

- `HTMLtoDOCXConverter.exe` - The standalone executable
- `install_standalone.bat` - One-click installer
- `uninstall_standalone.bat` - Easy uninstaller
- `test_converter.bat` - Test the installation

## 🚀 **Installation (Super Simple)**

### **On Any Windows System:**

1. **Copy the files** to any folder on the target computer
2. **Right-click** `install_standalone.bat`
3. **Select "Run as administrator"**
4. **That's it!** The service is now running

### **What Happens:**

- ✅ Installs to `C:\Program Files\HTMLtoDOCXConverter\`
- ✅ Sets up Windows service automatically
- ✅ Starts monitoring your Downloads folder
- ✅ No Python or dependencies needed

## 🧪 **Testing**

After installation, test it works:

1. **Right-click** `test_converter.bat`
2. **Select "Run as administrator"**
3. It will create a sample HTML file and convert it

## 🛠️ **Service Management**

### **Stop the Service:**

```cmd
"C:\Program Files\HTMLtoDOCXConverter\HTMLtoDOCXConverter.exe" stop
```

### **Start the Service:**

```cmd
"C:\Program Files\HTMLtoDOCXConverter\HTMLtoDOCXConverter.exe" start
```

### **Remove the Service:**

```cmd
"C:\Program Files\HTMLtoDOCXConverter\HTMLtoDOCXConverter.exe" remove
```

### **Or use the uninstaller:**

Right-click `uninstall_standalone.bat` → "Run as administrator"

## 📋 **Requirements**

- **Windows 10/11** (64-bit recommended)
- **Administrator privileges** (for installation only)
- **Downloads folder** (standard Windows location)

## 🔧 **Building the Standalone Executable**

### **If you want to build it yourself:**

1. **Install Python** (only needed for building, not for running)
2. **Run the build script:**
   ```cmd
   build_standalone.bat
   ```
3. **Wait for completion** (takes a few minutes)
4. **Use the generated files** on any Windows system

### **What the build process does:**

- Packages Python interpreter
- Includes all required libraries
- Creates single executable file
- Generates installer scripts

## 📁 **File Locations**

### **After Installation:**

- **Executable:** `C:\Program Files\HTMLtoDOCXConverter\HTMLtoDOCXConverter.exe`
- **Logs:** `C:\ProgramData\HTMLConverter\logs\html_converter.log`
- **Service:** Windows Services (HTMLtoDOCXConverter)

### **Downloads Monitoring:**

- **Watches:** `%USERPROFILE%\Downloads\`
- **Converts:** `.html` files to `.docx`
- **Removes:** Original HTML files after conversion

## 🎨 **Features**

- **CSS Styling Support:** Preserves colors, fonts, alignment
- **Minimal Margins:** 0.5cm margins for maximum content area
- **Background Service:** Runs silently, no user interaction
- **Automatic Detection:** Converts files as soon as they download
- **Comprehensive Logging:** Detailed activity logs

## 🔍 **Troubleshooting**

### **"Access Denied"**

- Run installer as administrator
- Check Windows Defender settings

### **"Service Won't Start"**

- Check Windows Event Viewer
- Verify Downloads folder exists

### **"No Conversion Happening"**

- Check log file for errors
- Ensure HTML files are actually downloading

### **"File Not Found"**

- Verify executable is in Program Files
- Re-run installer if needed

## 💡 **Pro Tips**

1. **Test First:** Always run the test script after installation
2. **Check Logs:** Monitor the log file for any issues
3. **Backup:** Keep the installer files for reinstallation
4. **Network:** Works with local Downloads folder only

## 🔒 **Security Notes**

- **Local Only:** No network access or data transmission
- **Downloads Only:** Only monitors your Downloads folder
- **System Service:** Runs with system privileges
- **No External Dependencies:** Everything is self-contained

## 📞 **Support**

If you encounter issues:

1. Check the log file: `C:\ProgramData\HTMLConverter\logs\html_converter.log`
2. Run the test script to verify functionality
3. Reinstall using the uninstaller first, then installer

---

**That's it!** No Python, no dependencies, no drama. Just click and install! 🎉
