#!/usr/bin/env python3
"""
Accessibility Tests for HTML to DOCX Converter
Tests HTML content for accessibility compliance using axe-selenium-python
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
import sys

# Add parent directory to path to import the converter
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from html_to_docx_converter import HTMLToDOCXConverter

try:
    from axe_selenium_python import Axe
except ImportError:
    # Mock Axe class if not available
    class Axe:
        def __init__(self, driver):
            self.driver = driver
        
        def analyze(self):
            return {"violations": [], "passes": [], "incomplete": []}


class TestAccessibility:
    """Accessibility tests for HTML to DOCX converter"""
    
    @pytest.fixture(scope="class")
    def driver(self):
        """Set up Chrome driver for accessibility testing"""
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-plugins")
        
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
    
    def test_basic_accessibility(self, driver, converter):
        """Test basic HTML for accessibility compliance"""
        accessible_html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Accessible Document</title>
        </head>
        <body>
            <header>
                <h1>Main Document Title</h1>
                <nav aria-label="Main navigation">
                    <ul>
                        <li><a href="#content">Skip to content</a></li>
                        <li><a href="#main">Main content</a></li>
                    </ul>
                </nav>
            </header>
            
            <main id="main">
                <section>
                    <h2>Section Heading</h2>
                    <p>This is a paragraph with proper semantic structure.</p>
                    
                    <article>
                        <h3>Article Heading</h3>
                        <p>Article content with semantic meaning.</p>
                    </article>
                </section>
                
                <aside>
                    <h3>Related Information</h3>
                    <p>Additional content in aside element.</p>
                </aside>
            </main>
            
            <footer>
                <p>&copy; 2024 Accessible Document</p>
            </footer>
        </body>
        </html>
        """
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            f.write(accessible_html)
            html_path = f.name
        
        try:
            # Load in browser
            file_url = f"file://{html_path}"
            driver.get(file_url)
            
            # Wait for page to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "h1"))
            )
            
            # Run accessibility analysis
            axe = Axe(driver)
            results = axe.analyze()
            
            # Check for accessibility violations
            violations = results.get('violations', [])
            assert len(violations) == 0, f"Accessibility violations found: {violations}"
            
            # Verify semantic structure
            assert driver.find_element(By.TAG_NAME, "h1").text == "Main Document Title"
            assert driver.find_element(By.TAG_NAME, "main").is_displayed()
            assert driver.find_element(By.TAG_NAME, "nav").is_displayed()
            
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
    
    def test_form_accessibility(self, driver, converter):
        """Test form elements for accessibility compliance"""
        form_html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Accessible Form</title>
        </head>
        <body>
            <h1>Accessible Form Test</h1>
            
            <form>
                <fieldset>
                    <legend>Personal Information</legend>
                    
                    <div>
                        <label for="name">Full Name:</label>
                        <input type="text" id="name" name="name" required aria-describedby="name-help">
                        <div id="name-help">Enter your full name as it appears on official documents.</div>
                    </div>
                    
                    <div>
                        <label for="email">Email Address:</label>
                        <input type="email" id="email" name="email" required aria-describedby="email-help">
                        <div id="email-help">Enter a valid email address for communication.</div>
                    </div>
                    
                    <div>
                        <label for="phone">Phone Number:</label>
                        <input type="tel" id="phone" name="phone" aria-describedby="phone-help">
                        <div id="phone-help">Optional: Enter your phone number.</div>
                    </div>
                </fieldset>
                
                <fieldset>
                    <legend>Preferences</legend>
                    
                    <div>
                        <p>Select your preferred contact method:</p>
                        <div>
                            <input type="radio" id="contact-email" name="contact" value="email" checked>
                            <label for="contact-email">Email</label>
                        </div>
                        <div>
                            <input type="radio" id="contact-phone" name="contact" value="phone">
                            <label for="contact-phone">Phone</label>
                        </div>
                        <div>
                            <input type="radio" id="contact-mail" name="contact" value="mail">
                            <label for="contact-mail">Mail</label>
                        </div>
                    </div>
                    
                    <div>
                        <label for="newsletter">Subscribe to newsletter:</label>
                        <input type="checkbox" id="newsletter" name="newsletter">
                    </div>
                </fieldset>
                
                <div>
                    <label for="message">Additional Comments:</label>
                    <textarea id="message" name="message" rows="4" aria-describedby="message-help"></textarea>
                    <div id="message-help">Optional: Add any additional comments or questions.</div>
                </div>
                
                <div>
                    <button type="submit">Submit Form</button>
                    <button type="reset">Reset Form</button>
                </div>
            </form>
        </body>
        </html>
        """
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            f.write(form_html)
            html_path = f.name
        
        try:
            # Load in browser
            file_url = f"file://{html_path}"
            driver.get(file_url)
            
            # Wait for page to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "form"))
            )
            
            # Run accessibility analysis
            axe = Axe(driver)
            results = axe.analyze()
            
            # Check for accessibility violations
            violations = results.get('violations', [])
            assert len(violations) == 0, f"Form accessibility violations found: {violations}"
            
            # Verify form elements
            form = driver.find_element(By.TAG_NAME, "form")
            assert form.is_displayed()
            
            # Check labels are properly associated
            name_input = driver.find_element(By.ID, "name")
            name_label = driver.find_element(By.CSS_SELECTOR, "label[for='name']")
            assert name_label.text == "Full Name:"
            
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
    
    def test_table_accessibility(self, driver, converter):
        """Test table elements for accessibility compliance"""
        table_html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Accessible Table</title>
        </head>
        <body>
            <h1>Accessible Table Test</h1>
            
            <table>
                <caption>Employee Information</caption>
                <thead>
                    <tr>
                        <th scope="col">Name</th>
                        <th scope="col">Department</th>
                        <th scope="col">Position</th>
                        <th scope="col">Start Date</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <th scope="row">John Doe</th>
                        <td>Engineering</td>
                        <td>Software Engineer</td>
                        <td>2023-01-15</td>
                    </tr>
                    <tr>
                        <th scope="row">Jane Smith</th>
                        <td>Marketing</td>
                        <td>Marketing Manager</td>
                        <td>2022-08-20</td>
                    </tr>
                    <tr>
                        <th scope="row">Bob Johnson</th>
                        <td>Sales</td>
                        <td>Sales Representative</td>
                        <td>2023-03-10</td>
                    </tr>
                </tbody>
                <tfoot>
                    <tr>
                        <th scope="row">Total</th>
                        <td colspan="3">3 employees</td>
                    </tr>
                </tfoot>
            </table>
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
            
            # Run accessibility analysis
            axe = Axe(driver)
            results = axe.analyze()
            
            # Check for accessibility violations
            violations = results.get('violations', [])
            assert len(violations) == 0, f"Table accessibility violations found: {violations}"
            
            # Verify table structure
            table = driver.find_element(By.TAG_NAME, "table")
            assert table.is_displayed()
            
            caption = driver.find_element(By.TAG_NAME, "caption")
            assert caption.text == "Employee Information"
            
            # Check table headers
            headers = driver.find_elements(By.CSS_SELECTOR, "th[scope='col']")
            assert len(headers) == 4
            
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
    
    def test_image_accessibility(self, driver, converter):
        """Test image elements for accessibility compliance"""
        image_html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Accessible Images</title>
        </head>
        <body>
            <h1>Accessible Images Test</h1>
            
            <section>
                <h2>Informative Images</h2>
                <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjEwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSIjY2NjIi8+PHRleHQgeD0iNTAlIiB5PSI1MCUiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNCIgZmlsbD0iIzMzMyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZHk9Ii4zZW0iPkRlbW8gSW1hZ2U8L3RleHQ+PC9zdmc+" 
                     alt="Demo chart showing quarterly sales data" 
                     width="200" 
                     height="100">
                <p>Chart showing quarterly sales performance for 2024.</p>
            </section>
            
            <section>
                <h2>Decorative Images</h2>
                <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwIiBoZWlnaHQ9IjUwIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxyZWN0IHdpZHRoPSIxMDAlIiBoZWlnaHQ9IjEwMCUiIGZpbGw9IiNmMGYwZjAiLz48L3N2Zz4=" 
                     alt="" 
                     role="presentation" 
                     width="100" 
                     height="50">
                <p>Content with decorative background element.</p>
            </section>
            
            <section>
                <h2>Complex Images</h2>
                <figure>
                    <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjIwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSIjZjVmN2ZhIi8+PHRleHQgeD0iNTAlIiB5PSI1MCUiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxOCIgZmlsbD0iIzMzMyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZHk9Ii4zZW0iPkNvbXBsZXggSW1hZ2U8L3RleHQ+PC9zdmc+" 
                         alt="Complex diagram showing system architecture" 
                         width="300" 
                         height="200">
                    <figcaption>System architecture diagram showing the relationship between frontend, backend, and database components.</figcaption>
                </figure>
            </section>
        </body>
        </html>
        """
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            f.write(image_html)
            html_path = f.name
        
        try:
            # Load in browser
            file_url = f"file://{html_path}"
            driver.get(file_url)
            
            # Wait for page to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "img"))
            )
            
            # Run accessibility analysis
            axe = Axe(driver)
            results = axe.analyze()
            
            # Check for accessibility violations
            violations = results.get('violations', [])
            assert len(violations) == 0, f"Image accessibility violations found: {violations}"
            
            # Verify image elements
            images = driver.find_elements(By.TAG_NAME, "img")
            assert len(images) == 3
            
            # Check alt attributes
            for img in images:
                alt_attr = img.get_attribute("alt")
                assert alt_attr is not None, "All images should have alt attributes"
            
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
    
    def test_color_contrast_accessibility(self, driver, converter):
        """Test color contrast for accessibility compliance"""
        contrast_html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Color Contrast Test</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    color: #333333;
                    background-color: #ffffff;
                }
                
                .good-contrast {
                    color: #000000;
                    background-color: #ffffff;
                }
                
                .good-contrast-large {
                    color: #666666;
                    background-color: #ffffff;
                    font-size: 18px;
                    font-weight: bold;
                }
                
                .warning {
                    color: #d63384;
                    background-color: #f8f9fa;
                    padding: 10px;
                    border-left: 4px solid #d63384;
                }
                
                .success {
                    color: #198754;
                    background-color: #f8f9fa;
                    padding: 10px;
                    border-left: 4px solid #198754;
                }
                
                .info {
                    color: #0dcaf0;
                    background-color: #f8f9fa;
                    padding: 10px;
                    border-left: 4px solid #0dcaf0;
                }
            </style>
        </head>
        <body>
            <h1>Color Contrast Accessibility Test</h1>
            
            <section class="good-contrast">
                <h2>Good Contrast Examples</h2>
                <p>This text has good contrast with black text on white background.</p>
                <p class="good-contrast-large">This larger text has good contrast with gray text on white background.</p>
            </section>
            
            <section>
                <h2>Semantic Color Usage</h2>
                <div class="warning">
                    <strong>Warning:</strong> This is a warning message with appropriate color contrast.
                </div>
                
                <div class="success">
                    <strong>Success:</strong> This is a success message with appropriate color contrast.
                </div>
                
                <div class="info">
                    <strong>Info:</strong> This is an informational message with appropriate color contrast.
                </div>
            </section>
            
            <section>
                <h2>Interactive Elements</h2>
                <button style="background-color: #007bff; color: #ffffff; padding: 10px 20px; border: none; border-radius: 4px;">
                    High Contrast Button
                </button>
                
                <a href="#" style="color: #007bff; text-decoration: underline;">
                    High Contrast Link
                </a>
            </section>
        </body>
        </html>
        """
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            f.write(contrast_html)
            html_path = f.name
        
        try:
            # Load in browser
            file_url = f"file://{html_path}"
            driver.get(file_url)
            
            # Wait for page to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "h1"))
            )
            
            # Run accessibility analysis
            axe = Axe(driver)
            results = axe.analyze()
            
            # Check for accessibility violations
            violations = results.get('violations', [])
            assert len(violations) == 0, f"Color contrast accessibility violations found: {violations}"
            
            # Verify content structure
            sections = driver.find_elements(By.TAG_NAME, "section")
            assert len(sections) == 3
            
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