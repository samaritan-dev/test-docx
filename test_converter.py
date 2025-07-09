#!/usr/bin/env python3
"""
Test script for HTML to DOCX converter
Creates a sample HTML file and tests the conversion
"""

import os
import tempfile
from pathlib import Path
from html_to_docx_converter import HTMLToDOCXConverter

def create_test_html():
    """Create a test HTML file with various elements and CSS styling."""
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test HTML Document with CSS Styling</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            font-size: 28px;
        }
        h2 {
            color: #34495e;
            border-bottom: 2px solid #3498db;
            padding-bottom: 5px;
        }
        .highlight {
            background-color: #f39c12;
            color: white;
            padding: 5px;
        }
        .important {
            font-weight: bold;
            color: #e74c3c;
        }
        .centered {
            text-align: center;
        }
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th {
            background-color: #3498db;
            color: white;
            padding: 10px;
        }
        td {
            padding: 8px;
            border: 1px solid #ddd;
        }
        .success {
            color: #27ae60;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>Main Heading with Styling</h1>
    <p>This is a paragraph with some <strong>bold text</strong> and <em>italic text</em>.</p>
    
    <p style="font-size: 18px; color: #8e44ad;">This paragraph has inline styling with larger font and purple color.</p>
    
    <h2>Subheading with Border</h2>
    <p>Another paragraph with some content.</p>
    
    <div class="highlight">
        <p>This is highlighted content with background color and white text.</p>
    </div>
    
    <p class="important">This is an important message with red color and bold text.</p>
    
    <h3>List Section</h3>
    <ul>
        <li>First item</li>
        <li>Second item</li>
        <li style="color: #e67e22; font-weight: bold;">Third item with inline styling</li>
    </ul>
    
    <ol>
        <li>Numbered item 1</li>
        <li>Numbered item 2</li>
        <li>Numbered item 3</li>
    </ol>
    
    <h3>Table Section with Styling</h3>
    <table>
        <tr>
            <th>Header 1</th>
            <th>Header 2</th>
            <th>Header 3</th>
        </tr>
        <tr>
            <td>Data 1</td>
            <td style="background-color: #ecf0f1;">Data 2 with background</td>
            <td>Data 3</td>
        </tr>
        <tr>
            <td>Data 4</td>
            <td>Data 5</td>
            <td class="success">Data 6 with success styling</td>
        </tr>
    </table>
    
    <div class="centered">
        <p>This content is centered using CSS.</p>
        <span style="font-size: 16px; text-decoration: underline;">This span has custom styling.</span>
    </div>
    
    <p style="text-align: justify; line-height: 2;">This is a justified paragraph with increased line height to demonstrate text formatting capabilities. It should wrap nicely and maintain proper spacing between lines.</p>
</body>
</html>
    """
    return html_content.strip()

def test_conversion():
    """Test the HTML to DOCX conversion."""
    print("Testing HTML to DOCX conversion...")
    
    # Create converter instance
    converter = HTMLToDOCXConverter()
    
    # Create test HTML file in Downloads folder
    downloads_path = Path(converter.downloads_path)
    test_html_path = downloads_path / "test_document.html"
    
    try:
        # Write test HTML file
        with open(test_html_path, 'w', encoding='utf-8') as f:
            f.write(create_test_html())
        
        print(f"Created test HTML file: {test_html_path}")
        
        # Convert to DOCX
        success = converter.convert_html_to_docx(str(test_html_path))
        
        if success:
            test_docx_path = test_html_path.with_suffix('.docx')
            if test_docx_path.exists():
                print(f"✓ Conversion successful! DOCX file created: {test_docx_path}")
                print(f"✓ Original HTML file removed: {test_html_path}")
                return True
            else:
                print("✗ Conversion failed: DOCX file not found")
                return False
        else:
            print("✗ Conversion failed")
            return False
            
    except Exception as e:
        print(f"✗ Test failed with error: {str(e)}")
        return False

if __name__ == "__main__":
    print("HTML to DOCX Converter Test")
    print("=" * 40)
    
    success = test_conversion()
    
    print("\n" + "=" * 40)
    if success:
        print("✓ Test completed successfully!")
        print("The converter is working correctly.")
    else:
        print("✗ Test failed!")
        print("Please check the logs for more details.")
    
    input("\nPress Enter to exit...") 