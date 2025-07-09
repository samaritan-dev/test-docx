#!/usr/bin/env python3
"""
Comprehensive test suite for HTML to DOCX Converter
"""

import pytest
import tempfile
import os
from pathlib import Path
from unittest.mock import patch, MagicMock
import sys
import os

# Add parent directory to path to import the converter
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from html_to_docx_converter import HTMLToDOCXConverter


class TestHTMLToDOCXConverter:
    """Test cases for HTMLToDOCXConverter class"""
    
    @pytest.fixture
    def converter(self):
        """Create a converter instance for testing"""
        return HTMLToDOCXConverter()
    
    @pytest.fixture
    def sample_html(self):
        """Sample HTML content for testing"""
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Test Document</title>
            <style>
                body { font-family: Arial, sans-serif; }
                h1 { color: #2c3e50; }
                .highlight { background-color: #f39c12; }
            </style>
        </head>
        <body>
            <h1>Test Heading</h1>
            <p>This is a test paragraph with <strong>bold</strong> and <em>italic</em> text.</p>
            <ul>
                <li>List item 1</li>
                <li>List item 2</li>
            </ul>
            <table border="1">
                <tr><th>Header 1</th><th>Header 2</th></tr>
                <tr><td>Data 1</td><td>Data 2</td></tr>
            </table>
        </body>
        </html>
        """
    
    def test_converter_initialization(self, converter):
        """Test converter initialization"""
        assert converter is not None
        assert hasattr(converter, 'downloads_path')
        assert hasattr(converter, 'logger')
        assert Path(converter.downloads_path).exists()
    
    def test_get_downloads_path(self, converter):
        """Test downloads path detection"""
        downloads_path = converter._get_downloads_path()
        assert downloads_path is not None
        assert isinstance(downloads_path, str)
        assert Path(downloads_path).exists()
    
    def test_parse_inline_css(self, converter):
        """Test inline CSS parsing"""
        css_string = "color: #ff0000; font-size: 16px; font-weight: bold;"
        styles = converter._parse_inline_css(css_string)
        
        assert styles['color'] == '#ff0000'
        assert styles['font-size'] == '16px'
        assert styles['font-weight'] == 'bold'
    
    def test_parse_css_rules(self, converter):
        """Test CSS rules parsing"""
        css_text = """
        h1 { color: #2c3e50; font-size: 24px; }
        .highlight { background-color: #f39c12; }
        """
        styles = converter._parse_css_rules(css_text)
        
        assert 'h1' in styles
        assert '.highlight' in styles
        assert styles['h1']['color'] == '#2c3e50'
        assert styles['.highlight']['background-color'] == '#f39c12'
    
    def test_extract_css_styles(self, converter):
        """Test CSS style extraction from HTML"""
        html_content = """
        <html>
        <head>
            <style>
                body { font-family: Arial; }
                h1 { color: red; }
            </style>
        </head>
        <body>
            <h1 style="font-size: 18px;">Title</h1>
            <p>Content</p>
        </body>
        </html>
        """
        
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        css_styles = converter._extract_css_styles(soup)
        
        assert css_styles is not None
        assert isinstance(css_styles, dict)
    
    def test_basic_html_conversion(self, converter, sample_html):
        """Test basic HTML to DOCX conversion"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            f.write(sample_html)
            html_path = f.name
        
        try:
            success = converter.convert_html_to_docx(html_path)
            assert success is True
            
            # Check if DOCX file was created
            docx_path = Path(html_path).with_suffix('.docx')
            assert docx_path.exists()
            
            # Check if original HTML was removed
            assert not Path(html_path).exists()
            
        finally:
            # Cleanup
            if Path(html_path).exists():
                Path(html_path).unlink()
            docx_path = Path(html_path).with_suffix('.docx')
            if docx_path.exists():
                docx_path.unlink()
    
    def test_html_with_css_styling(self, converter):
        """Test HTML conversion with CSS styling"""
        html_with_css = """
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                h1 { color: #2c3e50; text-align: center; }
                p { font-size: 16px; line-height: 1.5; }
                .highlight { background-color: #f39c12; color: white; }
            </style>
        </head>
        <body>
            <h1>Styled Heading</h1>
            <p>This paragraph has <span style="color: #e74c3c; font-weight: bold;">colored text</span>.</p>
            <div class="highlight">Highlighted content</div>
        </body>
        </html>
        """
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            f.write(html_with_css)
            html_path = f.name
        
        try:
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
    
    def test_html_with_tables(self, converter):
        """Test HTML conversion with tables"""
        html_with_table = """
        <!DOCTYPE html>
        <html>
        <head><title>Table Test</title></head>
        <body>
            <table border="1">
                <tr>
                    <th>Name</th>
                    <th>Age</th>
                    <th>City</th>
                </tr>
                <tr>
                    <td>John</td>
                    <td>25</td>
                    <td>New York</td>
                </tr>
                <tr>
                    <td>Jane</td>
                    <td>30</td>
                    <td>London</td>
                </tr>
            </table>
        </body>
        </html>
        """
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            f.write(html_with_table)
            html_path = f.name
        
        try:
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
    
    def test_html_with_lists(self, converter):
        """Test HTML conversion with lists"""
        html_with_lists = """
        <!DOCTYPE html>
        <html>
        <head><title>List Test</title></head>
        <body>
            <h2>Unordered List</h2>
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
                <li>Item 3</li>
            </ul>
            
            <h2>Ordered List</h2>
            <ol>
                <li>First item</li>
                <li>Second item</li>
                <li>Third item</li>
            </ol>
        </body>
        </html>
        """
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            f.write(html_with_lists)
            html_path = f.name
        
        try:
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
    
    def test_invalid_html_file(self, converter):
        """Test handling of invalid HTML file"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            f.write("This is not valid HTML content")
            html_path = f.name
        
        try:
            success = converter.convert_html_to_docx(html_path)
            # Should handle gracefully even with invalid HTML
            assert isinstance(success, bool)
            
        finally:
            # Cleanup
            if Path(html_path).exists():
                Path(html_path).unlink()
            docx_path = Path(html_path).with_suffix('.docx')
            if docx_path.exists():
                docx_path.unlink()
    
    def test_nonexistent_file(self, converter):
        """Test handling of nonexistent file"""
        success = converter.convert_html_to_docx("nonexistent_file.html")
        assert success is False
    
    @patch('pathlib.Path.exists')
    def test_downloads_path_not_exists(self, mock_exists, converter):
        """Test handling when Downloads path doesn't exist"""
        mock_exists.return_value = False
        
        # Should handle gracefully
        downloads_path = converter._get_downloads_path()
        assert downloads_path is not None


class TestFileSystemHandler:
    """Test cases for file system event handling"""
    
    @pytest.fixture
    def converter(self):
        return HTMLToDOCXConverter()
    
    @pytest.fixture
    def handler(self, converter):
        from html_to_docx_converter import DownloadFolderHandler
        return DownloadFolderHandler(converter)
    
    def test_handler_initialization(self, handler, converter):
        """Test file system handler initialization"""
        assert handler.converter == converter
        assert handler.logger == converter.logger
    
    @patch('html_to_docx_converter.HTMLToDOCXConverter.convert_html_to_docx')
    def test_on_created_html_file(self, mock_convert, handler):
        """Test handling of HTML file creation event"""
        from watchdog.events import FileCreatedEvent
        
        # Mock event
        event = MagicMock()
        event.is_directory = False
        event.src_path = "/path/to/test.html"
        
        # Mock Path
        with patch('pathlib.Path') as mock_path:
            mock_path_instance = MagicMock()
            mock_path_instance.suffix = '.html'
            mock_path.return_value = mock_path_instance
            
            # Test the handler
            handler.on_created(event)
            
            # Verify conversion was called
            mock_convert.assert_called_once_with("/path/to/test.html")
    
    def test_on_created_non_html_file(self, handler):
        """Test handling of non-HTML file creation event"""
        from watchdog.events import FileCreatedEvent
        
        # Mock event
        event = MagicMock()
        event.is_directory = False
        event.src_path = "/path/to/test.txt"
        
        # Mock Path
        with patch('pathlib.Path') as mock_path:
            mock_path_instance = MagicMock()
            mock_path_instance.suffix = '.txt'
            mock_path.return_value = mock_path_instance
            
            # Test the handler
            handler.on_created(event)
            
            # Should not trigger conversion for non-HTML files


if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 