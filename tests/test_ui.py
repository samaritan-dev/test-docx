#!/usr/bin/env python3
"""
UI Tests for HTML to DOCX Converter using Selenium
"""

import pytest
import tempfile
import os
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import sys
import os

# Add parent directory to path to import the converter
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from html_to_docx_converter import HTMLToDOCXConverter


class TestUI:
    """UI tests for HTML to DOCX converter"""
    
    @pytest.fixture(scope="class")
    def driver(self):
        """Set up Chrome driver for UI testing"""
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        
        try:
            driver = webdriver.Chrome(options=chrome_options)
            yield driver
        finally:
            driver.quit()
    
    @pytest.fixture
    def converter(self):
        """Create converter instance"""
        return HTMLToDOCXConverter()
    
    def test_html_rendering_and_conversion(self, driver, converter):
        """Test HTML rendering in browser and conversion to DOCX"""
        # Create a simple HTML file
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>UI Test Document</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                h1 { color: #2c3e50; text-align: center; }
                .highlight { background-color: #f39c12; color: white; padding: 10px; }
                table { border-collapse: collapse; width: 100%; }
                th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
                th { background-color: #3498db; color: white; }
            </style>
        </head>
        <body>
            <h1>UI Test Document</h1>
            <p>This is a test paragraph with <strong>bold</strong> and <em>italic</em> text.</p>
            <div class="highlight">This is highlighted content</div>
            <table>
                <tr><th>Name</th><th>Value</th></tr>
                <tr><td>Test 1</td><td>Value 1</td></tr>
                <tr><td>Test 2</td><td>Value 2</td></tr>
            </table>
        </body>
        </html>
        """
        
        # Create temporary HTML file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            f.write(html_content)
            html_path = f.name
        
        try:
            # Load HTML in browser
            file_url = f"file://{html_path}"
            driver.get(file_url)
            
            # Wait for page to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "h1"))
            )
            
            # Verify HTML rendering
            title = driver.find_element(By.TAG_NAME, "h1").text
            assert "UI Test Document" in title
            
            # Verify styling is applied
            highlight_element = driver.find_element(By.CLASS_NAME, "highlight")
            assert highlight_element.is_displayed()
            
            # Test conversion to DOCX
            success = converter.convert_html_to_docx(html_path)
            assert success is True
            
            # Verify DOCX file was created
            docx_path = Path(html_path).with_suffix('.docx')
            assert docx_path.exists()
            
        finally:
            # Cleanup
            if Path(html_path).exists():
                Path(html_path).unlink()
            docx_path = Path(html_path).with_suffix('.docx')
            if docx_path.exists():
                docx_path.unlink()
    
    def test_complex_html_styling(self, driver, converter):
        """Test complex HTML with advanced CSS styling"""
        complex_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Complex Styling Test</title>
            <style>
                body { 
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                }
                h1 { 
                    color: #2c3e50;
                    text-align: center;
                    border-bottom: 3px solid #3498db;
                    padding-bottom: 10px;
                }
                h2 { 
                    color: #34495e;
                    margin-top: 30px;
                }
                .container {
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 20px;
                    border-radius: 10px;
                    margin: 20px 0;
                }
                .button {
                    background-color: #e74c3c;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    font-weight: bold;
                }
                .button:hover {
                    background-color: #c0392b;
                }
                .grid {
                    display: grid;
                    grid-template-columns: repeat(3, 1fr);
                    gap: 20px;
                    margin: 20px 0;
                }
                .grid-item {
                    background-color: #ecf0f1;
                    padding: 15px;
                    border-radius: 5px;
                    text-align: center;
                }
            </style>
        </head>
        <body>
            <h1>Complex Styling Test</h1>
            <p>This document tests various CSS features and styling capabilities.</p>
            
            <div class="container">
                <h2>Gradient Background</h2>
                <p>This section has a gradient background with white text.</p>
            </div>
            
            <div class="grid">
                <div class="grid-item">Grid Item 1</div>
                <div class="grid-item">Grid Item 2</div>
                <div class="grid-item">Grid Item 3</div>
            </div>
            
            <button class="button">Test Button</button>
            
            <h2>Typography Test</h2>
            <p>This paragraph tests <strong>bold text</strong>, <em>italic text</em>, and <u>underlined text</u>.</p>
            <p>It also tests <span style="color: #e74c3c; font-size: 18px;">colored and sized text</span>.</p>
        </body>
        </html>
        """
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            f.write(complex_html)
            html_path = f.name
        
        try:
            # Load in browser
            file_url = f"file://{html_path}"
            driver.get(file_url)
            
            # Wait for page to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "container"))
            )
            
            # Verify complex styling
            container = driver.find_element(By.CLASS_NAME, "container")
            assert container.is_displayed()
            
            grid_items = driver.find_elements(By.CLASS_NAME, "grid-item")
            assert len(grid_items) == 3
            
            button = driver.find_element(By.CLASS_NAME, "button")
            assert button.is_displayed()
            
            # Test conversion
            success = converter.convert_html_to_docx(html_path)
            assert success is True
            
            docx_path = Path(html_path).with_suffix('.docx')
            assert docx_path.exists()
            
        finally:
            # Cleanup
            if Path(html_path).exists():
                Path(html_path).unlink()
            docx_path = Path(html_path).with_suffix('.docx')
            if docx_path.exists():
                docx_path.unlink()
    
    def test_responsive_design(self, driver, converter):
        """Test responsive design elements"""
        responsive_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Responsive Design Test</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body { 
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 20px;
                }
                .responsive-container {
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 20px;
                }
                .flex-container {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 20px;
                }
                .flex-item {
                    flex: 1;
                    min-width: 300px;
                    background-color: #f8f9fa;
                    padding: 20px;
                    border-radius: 8px;
                    border: 1px solid #dee2e6;
                }
                @media (max-width: 768px) {
                    .flex-item {
                        min-width: 100%;
                    }
                }
            </style>
        </head>
        <body>
            <div class="responsive-container">
                <h1>Responsive Design Test</h1>
                <div class="flex-container">
                    <div class="flex-item">
                        <h3>Section 1</h3>
                        <p>This is the first section with responsive design.</p>
                    </div>
                    <div class="flex-item">
                        <h3>Section 2</h3>
                        <p>This is the second section with responsive design.</p>
                    </div>
                    <div class="flex-item">
                        <h3>Section 3</h3>
                        <p>This is the third section with responsive design.</p>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            f.write(responsive_html)
            html_path = f.name
        
        try:
            # Load in browser
            file_url = f"file://{html_path}"
            driver.get(file_url)
            
            # Wait for page to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "flex-container"))
            )
            
            # Verify responsive elements
            flex_items = driver.find_elements(By.CLASS_NAME, "flex-item")
            assert len(flex_items) == 3
            
            # Test conversion
            success = converter.convert_html_to_docx(html_path)
            assert success is True
            
            docx_path = Path(html_path).with_suffix('.docx')
            assert docx_path.exists()
            
        finally:
            # Cleanup
            if Path(html_path).exists():
                Path(html_path).unlink()
            docx_path = Path(html_path).with_suffix('.docx')
            if docx_path.exists():
                docx_path.unlink()


if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 