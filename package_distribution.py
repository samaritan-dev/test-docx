#!/usr/bin/env python3
"""
Package the standalone distribution for easy sharing
"""

import os
import shutil
import zipfile
from pathlib import Path
from datetime import datetime

def package_distribution():
    """Package the standalone distribution."""
    print("Packaging Standalone Distribution...")
    print("=" * 40)
    
    # Check if dist folder exists
    dist_path = Path("dist")
    if not dist_path.exists():
        print("❌ dist/ folder not found. Please run build_standalone.bat first.")
        return False
    
    # Create distribution package
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    package_name = f"HTMLtoDOCXConverter_Standalone_{timestamp}"
    package_path = Path(package_name)
    
    # Create package directory
    package_path.mkdir(exist_ok=True)
    
    # Copy files to package
    files_to_copy = [
        "HTMLtoDOCXConverter.exe",
        "install.bat",
        "uninstall.bat", 
        "test.bat",
        "README_STANDALONE.txt"
    ]
    
    print("Copying files...")
    for file_name in files_to_copy:
        src = dist_path / file_name
        dst = package_path / file_name
        
        if src.exists():
            shutil.copy2(src, dst)
            print(f"✅ {file_name}")
        else:
            print(f"⚠️  {file_name} not found")
    
    # Create ZIP file
    zip_name = f"{package_name}.zip"
    print(f"\nCreating ZIP file: {zip_name}")
    
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_path in package_path.rglob('*'):
            if file_path.is_file():
                arcname = file_path.relative_to(package_path)
                zipf.write(file_path, arcname)
                print(f"📦 Added: {arcname}")
    
    # Clean up package directory
    shutil.rmtree(package_path)
    
    print(f"\n✅ Distribution packaged successfully!")
    print(f"📦 Package: {zip_name}")
    print(f"📁 Size: {Path(zip_name).stat().st_size / 1024 / 1024:.1f} MB")
    
    return True

def main():
    """Main function."""
    success = package_distribution()
    
    if success:
        print("\n🎉 Ready for distribution!")
        print("Share the ZIP file with anyone - no Python required!")
    else:
        print("\n❌ Packaging failed.")

if __name__ == "__main__":
    main() 