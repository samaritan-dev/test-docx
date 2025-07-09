#!/usr/bin/env python3
"""
Extensive UI Test Runner
Runs comprehensive UI tests for HTML to DOCX converter
"""

import os
import sys
import subprocess
import argparse
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import json

def run_test_command(cmd, test_name):
    """Run a test command and return results"""
    print(f"🚀 Running {test_name}...")
    start_time = time.time()
    
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )
        
        duration = time.time() - start_time
        
        if result.returncode == 0:
            print(f"✅ {test_name} completed successfully in {duration:.2f}s")
            return {
                'test': test_name,
                'status': 'PASSED',
                'duration': duration,
                'output': result.stdout
            }
        else:
            print(f"❌ {test_name} failed in {duration:.2f}s")
            return {
                'test': test_name,
                'status': 'FAILED',
                'duration': duration,
                'output': result.stdout,
                'error': result.stderr
            }
            
    except subprocess.TimeoutExpired:
        print(f"⏰ {test_name} timed out after 5 minutes")
        return {
            'test': test_name,
            'status': 'TIMEOUT',
            'duration': 300,
            'error': 'Test timed out after 5 minutes'
        }
    except Exception as e:
        print(f"💥 {test_name} encountered an error: {e}")
        return {
            'test': test_name,
            'status': 'ERROR',
            'duration': 0,
            'error': str(e)
        }

def run_basic_ui_tests(browsers=None):
    """Run basic UI element tests"""
    if browsers is None:
        browsers = ['chrome', 'firefox']
    
    tests = []
    for browser in browsers:
        cmd = f"python -m pytest tests/test_ui_extensive.py::TestExtensiveUI::test_basic_html_elements --browser={browser} --html=reports/basic-ui-{browser}.html --self-contained-html -v"
        tests.append((cmd, f"Basic UI Test ({browser})"))
    
    return tests

def run_complex_css_tests(browsers=None):
    """Run complex CSS styling tests"""
    if browsers is None:
        browsers = ['chrome', 'firefox']
    
    tests = []
    for browser in browsers:
        cmd = f"python -m pytest tests/test_ui_extensive.py::TestExtensiveUI::test_complex_css_styling --browser={browser} --html=reports/complex-css-{browser}.html --self-contained-html -v"
        tests.append((cmd, f"Complex CSS Test ({browser})"))
    
    return tests

def run_responsive_tests():
    """Run responsive design tests"""
    viewports = ['1920x1080', '1366x768', '768x1024', '375x667']
    
    tests = []
    for viewport in viewports:
        cmd = f"python -m pytest tests/test_ui_extensive.py::TestExtensiveUI::test_responsive_design --viewport={viewport} --html=reports/responsive-{viewport}.html --self-contained-html -v"
        tests.append((cmd, f"Responsive Test ({viewport})"))
    
    return tests

def run_typography_tests():
    """Run typography and text effects tests"""
    cmd = "python -m pytest tests/test_ui_extensive.py::TestExtensiveUI::test_typography_and_text_effects --html=reports/typography-tests.html --self-contained-html -v"
    return [(cmd, "Typography Test")]

def run_tables_forms_tests(browsers=None):
    """Run tables and forms tests"""
    if browsers is None:
        browsers = ['chrome', 'firefox']
    
    tests = []
    for browser in browsers:
        cmd = f"python -m pytest tests/test_ui_extensive.py::TestExtensiveUI::test_tables_and_forms --browser={browser} --html=reports/tables-forms-{browser}.html --self-contained-html -v"
        tests.append((cmd, f"Tables & Forms Test ({browser})"))
    
    return tests

def run_accessibility_tests():
    """Run accessibility tests"""
    cmd = "python -m pytest tests/test_accessibility.py --html=reports/accessibility-tests.html --self-contained-html -v"
    return [(cmd, "Accessibility Test")]

def run_performance_tests():
    """Run performance tests"""
    cmd = "python -m pytest tests/test_ui_extensive.py --html=reports/performance-tests.html --self-contained-html -v --durations=10"
    return [(cmd, "Performance Test")]

def run_cross_browser_tests():
    """Run cross-browser compatibility tests"""
    browsers = ['chrome', 'firefox', 'edge']
    
    tests = []
    for browser in browsers:
        cmd = f"python -m pytest tests/test_ui_extensive.py --browser={browser} --html=reports/cross-browser-{browser}.html --self-contained-html -v"
        tests.append((cmd, f"Cross-Browser Test ({browser})"))
    
    return tests

def generate_test_summary(results):
    """Generate a test summary report"""
    total_tests = len(results)
    passed_tests = len([r for r in results if r['status'] == 'PASSED'])
    failed_tests = len([r for r in results if r['status'] == 'FAILED'])
    error_tests = len([r for r in results if r['status'] in ['ERROR', 'TIMEOUT']])
    
    total_duration = sum(r['duration'] for r in results)
    
    summary = {
        'summary': {
            'total_tests': total_tests,
            'passed_tests': passed_tests,
            'failed_tests': failed_tests,
            'error_tests': error_tests,
            'success_rate': (passed_tests / total_tests * 100) if total_tests > 0 else 0,
            'total_duration': total_duration
        },
        'results': results
    }
    
    return summary

def save_test_results(summary, output_file='test-results.json'):
    """Save test results to JSON file"""
    with open(output_file, 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"📊 Test results saved to {output_file}")

def print_test_summary(summary):
    """Print a formatted test summary"""
    s = summary['summary']
    
    print("\n" + "="*60)
    print("🧪 EXTENSIVE UI TEST RESULTS SUMMARY")
    print("="*60)
    print(f"Total Tests: {s['total_tests']}")
    print(f"Passed: {s['passed_tests']} ✅")
    print(f"Failed: {s['failed_tests']} ❌")
    print(f"Errors: {s['error_tests']} 💥")
    print(f"Success Rate: {s['success_rate']:.1f}%")
    print(f"Total Duration: {s['total_duration']:.2f}s")
    print("="*60)
    
    if s['failed_tests'] > 0 or s['error_tests'] > 0:
        print("\n❌ FAILED TESTS:")
        for result in summary['results']:
            if result['status'] in ['FAILED', 'ERROR', 'TIMEOUT']:
                print(f"  - {result['test']}: {result['status']}")
                if 'error' in result:
                    print(f"    Error: {result['error'][:100]}...")
    
    print("\n📁 Test reports available in the 'reports' directory")

def main():
    parser = argparse.ArgumentParser(description='Run extensive UI tests for HTML to DOCX converter')
    parser.add_argument('--test-type', choices=['all', 'basic', 'complex', 'responsive', 'typography', 'tables', 'accessibility', 'performance', 'cross-browser'], 
                       default='all', help='Type of tests to run')
    parser.add_argument('--browsers', nargs='+', choices=['chrome', 'firefox', 'edge'], 
                       default=['chrome', 'firefox'], help='Browsers to test')
    parser.add_argument('--parallel', action='store_true', help='Run tests in parallel')
    parser.add_argument('--output', default='test-results.json', help='Output file for test results')
    
    args = parser.parse_args()
    
    # Create reports directory
    Path('reports').mkdir(exist_ok=True)
    
    # Determine which tests to run
    all_tests = []
    
    if args.test_type in ['all', 'basic']:
        all_tests.extend(run_basic_ui_tests(args.browsers))
    
    if args.test_type in ['all', 'complex']:
        all_tests.extend(run_complex_css_tests(args.browsers))
    
    if args.test_type in ['all', 'responsive']:
        all_tests.extend(run_responsive_tests())
    
    if args.test_type in ['all', 'typography']:
        all_tests.extend(run_typography_tests())
    
    if args.test_type in ['all', 'tables']:
        all_tests.extend(run_tables_forms_tests(args.browsers))
    
    if args.test_type in ['all', 'accessibility']:
        all_tests.extend(run_accessibility_tests())
    
    if args.test_type in ['all', 'performance']:
        all_tests.extend(run_performance_tests())
    
    if args.test_type in ['all', 'cross-browser']:
        all_tests.extend(run_cross_browser_tests())
    
    print(f"🎯 Running {len(all_tests)} tests...")
    print(f"🧪 Test type: {args.test_type}")
    print(f"🌐 Browsers: {', '.join(args.browsers)}")
    print(f"⚡ Parallel execution: {args.parallel}")
    print()
    
    # Run tests
    results = []
    
    if args.parallel:
        # Run tests in parallel
        with ThreadPoolExecutor(max_workers=4) as executor:
            future_to_test = {
                executor.submit(run_test_command, cmd, name): (cmd, name) 
                for cmd, name in all_tests
            }
            
            for future in as_completed(future_to_test):
                result = future.result()
                results.append(result)
    else:
        # Run tests sequentially
        for cmd, name in all_tests:
            result = run_test_command(cmd, name)
            results.append(result)
    
    # Generate and save summary
    summary = generate_test_summary(results)
    save_test_results(summary, args.output)
    print_test_summary(summary)
    
    # Exit with appropriate code
    if summary['summary']['failed_tests'] > 0 or summary['summary']['error_tests'] > 0:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main() 