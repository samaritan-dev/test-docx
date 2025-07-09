#!/usr/bin/env python3
"""
Extensive UI Tests for HTML to DOCX Converter using Selenium
Comprehensive testing of HTML rendering, CSS styling, and conversion
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
from selenium.webdriver.common.action_chains import ActionChains
import sys
import os

# Add parent directory to path to import the converter
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from html_to_docx_converter import HTMLToDOCXConverter


class TestExtensiveUI:
    """Extensive UI tests for HTML to DOCX converter"""
    
    @pytest.fixture(scope="class")
    def driver(self):
        """Set up Chrome driver for UI testing"""
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-plugins")
        chrome_options.add_argument("--disable-images")  # Faster loading
        
        try:
            driver = webdriver.Chrome(options=chrome_options)
            driver.implicitly_wait(10)
            yield driver
        finally:
            driver.quit()
    
    @pytest.fixture
    def converter(self):
        """Create converter instance"""
        return HTMLToDOCXConverter()
    
    def test_basic_html_elements(self, driver, converter):
        """Test basic HTML elements rendering and conversion"""
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Basic Elements Test</title>
        </head>
        <body>
            <h1>Main Heading</h1>
            <h2>Sub Heading</h2>
            <h3>Section Heading</h3>
            <h4>Subsection Heading</h4>
            <h5>Minor Heading</h5>
            <h6>Smallest Heading</h6>
            
            <p>This is a paragraph with <strong>bold text</strong> and <em>italic text</em>.</p>
            <p>Another paragraph with <u>underlined text</u> and <mark>highlighted text</mark>.</p>
            
            <ul>
                <li>Unordered list item 1</li>
                <li>Unordered list item 2</li>
                <li>Unordered list item 3</li>
            </ul>
            
            <ol>
                <li>Ordered list item 1</li>
                <li>Ordered list item 2</li>
                <li>Ordered list item 3</li>
            </ol>
            
            <blockquote>This is a blockquote with some quoted text.</blockquote>
            
            <pre>This is preformatted text with spaces    and line breaks.</pre>
            
            <code>This is inline code</code>
        </body>
        </html>
        """
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            f.write(html_content)
            html_path = f.name
        
        try:
            # Load in browser
            file_url = f"file://{html_path}"
            driver.get(file_url)
            
            # Wait for page to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "h1"))
            )
            
            # Verify all elements are rendered
            assert driver.find_element(By.TAG_NAME, "h1").text == "Main Heading"
            assert driver.find_element(By.TAG_NAME, "h2").text == "Sub Heading"
            assert driver.find_element(By.TAG_NAME, "h3").text == "Section Heading"
            
            # Verify lists
            ul_items = driver.find_elements(By.CSS_SELECTOR, "ul li")
            assert len(ul_items) == 3
            
            ol_items = driver.find_elements(By.CSS_SELECTOR, "ol li")
            assert len(ol_items) == 3
            
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
    
    def test_complex_css_styling(self, driver, converter):
        """Test complex CSS styling and layout"""
        complex_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Complex CSS Test</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 20px;
                    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
                }
                
                .header {
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 30px;
                    border-radius: 15px;
                    text-align: center;
                    margin-bottom: 30px;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
                }
                
                .content-grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                    gap: 20px;
                    margin: 20px 0;
                }
                
                .card {
                    background: white;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                    border-left: 5px solid #667eea;
                }
                
                .highlight-box {
                    background: linear-gradient(45deg, #ff6b6b, #feca57);
                    color: white;
                    padding: 20px;
                    border-radius: 10px;
                    margin: 20px 0;
                    text-align: center;
                }
                
                .button {
                    background: linear-gradient(45deg, #667eea, #764ba2);
                    color: white;
                    padding: 12px 24px;
                    border: none;
                    border-radius: 25px;
                    cursor: pointer;
                    font-weight: bold;
                    transition: transform 0.3s ease;
                }
                
                .button:hover {
                    transform: translateY(-2px);
                }
                
                .text-effects {
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
                    font-size: 24px;
                    font-weight: bold;
                    color: #2c3e50;
                }
                
                .flex-container {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    background: #ecf0f1;
                    padding: 20px;
                    border-radius: 10px;
                    margin: 20px 0;
                }
                
                .flex-item {
                    background: white;
                    padding: 15px;
                    border-radius: 8px;
                    text-align: center;
                    flex: 1;
                    margin: 0 10px;
                }
                
                @media (max-width: 768px) {
                    .flex-container {
                        flex-direction: column;
                    }
                    .flex-item {
                        margin: 10px 0;
                    }
                }
            </style>
        </head>
        <body>
            <div class="header">
                <h1>Complex CSS Styling Test</h1>
                <p>Testing advanced CSS features and modern web design</p>
            </div>
            
            <div class="content-grid">
                <div class="card">
                    <h3>Card 1</h3>
                    <p>This is a styled card with shadow and border effects.</p>
                </div>
                <div class="card">
                    <h3>Card 2</h3>
                    <p>Another card with consistent styling and layout.</p>
                </div>
                <div class="card">
                    <h3>Card 3</h3>
                    <p>Third card demonstrating grid layout capabilities.</p>
                </div>
            </div>
            
            <div class="highlight-box">
                <h2>Highlighted Content</h2>
                <p>This section uses gradient backgrounds and special styling.</p>
            </div>
            
            <div class="flex-container">
                <div class="flex-item">
                    <h4>Flex Item 1</h4>
                    <p>Responsive flexbox layout</p>
                </div>
                <div class="flex-item">
                    <h4>Flex Item 2</h4>
                    <p>Adaptive design elements</p>
                </div>
                <div class="flex-item">
                    <h4>Flex Item 3</h4>
                    <p>Modern CSS features</p>
                </div>
            </div>
            
            <div class="text-effects">
                <p>Text with shadow effects and styling</p>
            </div>
            
            <button class="button">Interactive Button</button>
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
                EC.presence_of_element_located((By.CLASS_NAME, "header"))
            )
            
            # Verify complex styling elements
            header = driver.find_element(By.CLASS_NAME, "header")
            assert header.is_displayed()
            
            cards = driver.find_elements(By.CLASS_NAME, "card")
            assert len(cards) == 3
            
            flex_items = driver.find_elements(By.CLASS_NAME, "flex-item")
            assert len(flex_items) == 3
            
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
    
    def test_tables_and_forms(self, driver, converter):
        """Test complex tables and form elements"""
        table_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Tables and Forms Test</title>
            <style>
                table {
                    border-collapse: collapse;
                    width: 100%;
                    margin: 20px 0;
                }
                th, td {
                    border: 1px solid #ddd;
                    padding: 12px;
                    text-align: left;
                }
                th {
                    background-color: #4CAF50;
                    color: white;
                }
                tr:nth-child(even) {
                    background-color: #f2f2f2;
                }
                tr:hover {
                    background-color: #ddd;
                }
                .form-container {
                    background: #f9f9f9;
                    padding: 20px;
                    border-radius: 10px;
                    margin: 20px 0;
                }
                input, select, textarea {
                    width: 100%;
                    padding: 12px;
                    margin: 8px 0;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                    box-sizing: border-box;
                }
            </style>
        </head>
        <body>
            <h1>Tables and Forms Test</h1>
            
            <h2>Complex Table</h2>
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Age</th>
                        <th>City</th>
                        <th>Occupation</th>
                        <th>Salary</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>John Doe</td>
                        <td>30</td>
                        <td>New York</td>
                        <td>Software Engineer</td>
                        <td>$85,000</td>
                    </tr>
                    <tr>
                        <td>Jane Smith</td>
                        <td>28</td>
                        <td>Los Angeles</td>
                        <td>Designer</td>
                        <td>$75,000</td>
                    </tr>
                    <tr>
                        <td>Bob Johnson</td>
                        <td>35</td>
                        <td>Chicago</td>
                        <td>Manager</td>
                        <td>$95,000</td>
                    </tr>
                    <tr>
                        <td>Alice Brown</td>
                        <td>32</td>
                        <td>Houston</td>
                        <td>Analyst</td>
                        <td>$70,000</td>
                    </tr>
                </tbody>
            </table>
            
            <h2>Form Elements</h2>
            <div class="form-container">
                <form>
                    <label for="name">Name:</label>
                    <input type="text" id="name" name="name" value="John Doe">
                    
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" value="john@example.com">
                    
                    <label for="country">Country:</label>
                    <select id="country" name="country">
                        <option value="us">United States</option>
                        <option value="ca">Canada</option>
                        <option value="uk">United Kingdom</option>
                        <option value="au">Australia</option>
                    </select>
                    
                    <label for="message">Message:</label>
                    <textarea id="message" name="message" rows="4">This is a sample message for testing form elements.</textarea>
                </form>
            </div>
        </body>
        </html>
        """
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            f.write(table_html)
            html_path = f.name
        
        try:
            # Load in browser
            file_url = f"file://{html_path}"
            driver.get(file_url)
            
            # Wait for page to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "table"))
            )
            
            # Verify table elements
            table_rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
            assert len(table_rows) == 4
            
            table_cells = driver.find_elements(By.CSS_SELECTOR, "table td")
            assert len(table_cells) == 20  # 4 rows * 5 columns
            
            # Verify form elements
            form_inputs = driver.find_elements(By.CSS_SELECTOR, "input, select, textarea")
            assert len(form_inputs) >= 4
            
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
        """Test responsive design elements and media queries"""
        responsive_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Responsive Design Test</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                * {
                    box-sizing: border-box;
                }
                
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 20px;
                    background-color: #f4f4f4;
                }
                
                .container {
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 0 15px;
                }
                
                .header {
                    background: #333;
                    color: white;
                    text-align: center;
                    padding: 20px;
                    margin-bottom: 20px;
                }
                
                .nav {
                    background: #444;
                    padding: 10px;
                    margin-bottom: 20px;
                }
                
                .nav ul {
                    list-style: none;
                    padding: 0;
                    margin: 0;
                    display: flex;
                    justify-content: center;
                }
                
                .nav li {
                    margin: 0 15px;
                }
                
                .nav a {
                    color: white;
                    text-decoration: none;
                }
                
                .main-content {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 20px;
                }
                
                .sidebar {
                    flex: 1;
                    min-width: 250px;
                    background: white;
                    padding: 20px;
                    border-radius: 8px;
                }
                
                .content {
                    flex: 3;
                    min-width: 300px;
                    background: white;
                    padding: 20px;
                    border-radius: 8px;
                }
                
                .card-grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                    gap: 20px;
                    margin-top: 20px;
                }
                
                .card {
                    background: #fff;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                }
                
                .footer {
                    background: #333;
                    color: white;
                    text-align: center;
                    padding: 20px;
                    margin-top: 20px;
                }
                
                /* Mobile responsive */
                @media (max-width: 768px) {
                    .nav ul {
                        flex-direction: column;
                        text-align: center;
                    }
                    
                    .nav li {
                        margin: 5px 0;
                    }
                    
                    .main-content {
                        flex-direction: column;
                    }
                    
                    .sidebar, .content {
                        min-width: 100%;
                    }
                    
                    .card-grid {
                        grid-template-columns: 1fr;
                    }
                }
                
                /* Tablet responsive */
                @media (max-width: 1024px) and (min-width: 769px) {
                    .card-grid {
                        grid-template-columns: repeat(2, 1fr);
                    }
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Responsive Design Test</h1>
                    <p>Testing responsive layout and mobile compatibility</p>
                </div>
                
                <nav class="nav">
                    <ul>
                        <li><a href="#">Home</a></li>
                        <li><a href="#">About</a></li>
                        <li><a href="#">Services</a></li>
                        <li><a href="#">Contact</a></li>
                    </ul>
                </nav>
                
                <div class="main-content">
                    <aside class="sidebar">
                        <h3>Sidebar</h3>
                        <p>This is the sidebar content that adapts to different screen sizes.</p>
                        <ul>
                            <li>Sidebar item 1</li>
                            <li>Sidebar item 2</li>
                            <li>Sidebar item 3</li>
                        </ul>
                    </aside>
                    
                    <main class="content">
                        <h2>Main Content</h2>
                        <p>This is the main content area that responds to different screen sizes.</p>
                        
                        <div class="card-grid">
                            <div class="card">
                                <h4>Card 1</h4>
                                <p>Responsive card content</p>
                            </div>
                            <div class="card">
                                <h4>Card 2</h4>
                                <p>Another responsive card</p>
                            </div>
                            <div class="card">
                                <h4>Card 3</h4>
                                <p>Third responsive card</p>
                            </div>
                            <div class="card">
                                <h4>Card 4</h4>
                                <p>Fourth responsive card</p>
                            </div>
                        </div>
                    </main>
                </div>
                
                <footer class="footer">
                    <p>&copy; 2024 Responsive Design Test. All rights reserved.</p>
                </footer>
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
                EC.presence_of_element_located((By.CLASS_NAME, "header"))
            )
            
            # Verify responsive elements
            nav_items = driver.find_elements(By.CSS_SELECTOR, ".nav li")
            assert len(nav_items) == 4
            
            cards = driver.find_elements(By.CLASS_NAME, "card")
            assert len(cards) == 4
            
            sidebar = driver.find_element(By.CLASS_NAME, "sidebar")
            assert sidebar.is_displayed()
            
            content = driver.find_element(By.CLASS_NAME, "content")
            assert content.is_displayed()
            
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
    
    def test_typography_and_text_effects(self, driver, converter):
        """Test typography and text styling effects"""
        typography_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Typography Test</title>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&family=Open+Sans:wght@400;600&display=swap');
                
                body {
                    font-family: 'Roboto', sans-serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                }
                
                .text-variants {
                    margin: 20px 0;
                }
                
                .text-variants h1 {
                    font-family: 'Open Sans', sans-serif;
                    font-weight: 700;
                    font-size: 2.5em;
                    color: #2c3e50;
                    text-transform: uppercase;
                    letter-spacing: 2px;
                    margin-bottom: 10px;
                }
                
                .text-variants h2 {
                    font-weight: 600;
                    font-size: 1.8em;
                    color: #34495e;
                    border-bottom: 3px solid #3498db;
                    padding-bottom: 5px;
                }
                
                .text-variants h3 {
                    font-weight: 400;
                    font-size: 1.3em;
                    color: #7f8c8d;
                    font-style: italic;
                }
                
                .text-effects {
                    margin: 30px 0;
                }
                
                .shadow-text {
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
                    font-size: 24px;
                    font-weight: bold;
                    color: #e74c3c;
                }
                
                .gradient-text {
                    background: linear-gradient(45deg, #667eea, #764ba2);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    background-clip: text;
                    font-size: 28px;
                    font-weight: bold;
                }
                
                .outline-text {
                    color: white;
                    text-shadow: 
                        -1px -1px 0 #000,
                        1px -1px 0 #000,
                        -1px 1px 0 #000,
                        1px 1px 0 #000;
                    font-size: 26px;
                    font-weight: bold;
                }
                
                .paragraph-styles {
                    margin: 20px 0;
                }
                
                .paragraph-styles p {
                    margin: 15px 0;
                    padding: 10px;
                    border-left: 4px solid #3498db;
                    background: #f8f9fa;
                }
                
                .paragraph-styles .highlight {
                    background: #fff3cd;
                    border-color: #ffc107;
                }
                
                .paragraph-styles .warning {
                    background: #f8d7da;
                    border-color: #dc3545;
                }
                
                .paragraph-styles .success {
                    background: #d4edda;
                    border-color: #28a745;
                }
                
                .list-styles {
                    margin: 20px 0;
                }
                
                .list-styles ul {
                    list-style: none;
                    padding: 0;
                }
                
                .list-styles li {
                    padding: 8px 0;
                    border-bottom: 1px solid #eee;
                    position: relative;
                    padding-left: 20px;
                }
                
                .list-styles li:before {
                    content: "▶";
                    color: #3498db;
                    position: absolute;
                    left: 0;
                }
                
                .list-styles li:hover {
                    background: #f8f9fa;
                    padding-left: 25px;
                    transition: all 0.3s ease;
                }
            </style>
        </head>
        <body>
            <div class="text-variants">
                <h1>Typography Test</h1>
                <h2>Different Heading Styles</h2>
                <h3>With Various Font Weights and Sizes</h3>
            </div>
            
            <div class="text-effects">
                <p class="shadow-text">Text with Shadow Effects</p>
                <p class="gradient-text">Gradient Text Effect</p>
                <p class="outline-text">Text with Outline</p>
            </div>
            
            <div class="paragraph-styles">
                <p>This is a regular paragraph with standard styling and formatting.</p>
                <p class="highlight">This paragraph has a highlighted background with special styling.</p>
                <p class="warning">This paragraph has a warning style with red border and background.</p>
                <p class="success">This paragraph has a success style with green border and background.</p>
            </div>
            
            <div class="list-styles">
                <h3>Styled List Items</h3>
                <ul>
                    <li>List item with custom bullet and hover effects</li>
                    <li>Another item with smooth transitions</li>
                    <li>Third item demonstrating typography</li>
                    <li>Fourth item with consistent styling</li>
                </ul>
            </div>
            
            <div class="text-variants">
                <h2>Font Weight Variations</h2>
                <p style="font-weight: 300;">Light weight text (300)</p>
                <p style="font-weight: 400;">Regular weight text (400)</p>
                <p style="font-weight: 600;">Semi-bold weight text (600)</p>
                <p style="font-weight: 700;">Bold weight text (700)</p>
            </div>
        </body>
        </html>
        """
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            f.write(typography_html)
            html_path = f.name
        
        try:
            # Load in browser
            file_url = f"file://{html_path}"
            driver.get(file_url)
            
            # Wait for page to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "text-variants"))
            )
            
            # Verify typography elements
            headings = driver.find_elements(By.CSS_SELECTOR, "h1, h2, h3")
            assert len(headings) >= 3
            
            text_effects = driver.find_elements(By.CSS_SELECTOR, ".shadow-text, .gradient-text, .outline-text")
            assert len(text_effects) == 3
            
            list_items = driver.find_elements(By.CSS_SELECTOR, ".list-styles li")
            assert len(list_items) == 4
            
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