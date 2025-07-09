#!/usr/bin/env python3
"""
Comprehensive test runner for HTML to DOCX Converter
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path


def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n{'='*60}")
    print(f"🔄 {description}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print("✅ Success!")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed: {e}")
        if e.stdout:
            print("STDOUT:", e.stdout)
        if e.stderr:
            print("STDERR:", e.stderr)
        return False


def run_unit_tests():
    """Run unit tests"""
    return run_command(
        "python -m pytest tests/test_converter.py -v --cov=html_to_docx_converter --cov-report=term-missing",
        "Running Unit Tests"
    )


def run_ui_tests():
    """Run UI tests"""
    return run_command(
        "python -m pytest tests/test_ui.py -v",
        "Running UI Tests"
    )


def run_integration_tests():
    """Run integration tests"""
    return run_command(
        "python test_converter.py",
        "Running Integration Tests"
    )


def run_linting():
    """Run code linting"""
    return run_command(
        "flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics",
        "Running Code Linting"
    )


def run_format_check():
    """Run code format check"""
    return run_command(
        "black --check --diff .",
        "Running Code Format Check"
    )


def run_security_scan():
    """Run security scan"""
    return run_command(
        "bandit -r . -f json -o bandit-report.json",
        "Running Security Scan"
    )


def run_build_test():
    """Test standalone build"""
    return run_command(
        "python build_exe.py",
        "Testing Standalone Build"
    )


def run_all_tests():
    """Run all tests"""
    print("🚀 Starting Comprehensive Test Suite")
    print("="*60)
    
    tests = [
        ("Unit Tests", run_unit_tests),
        ("Integration Tests", run_integration_tests),
        ("Code Linting", run_linting),
        ("Code Format Check", run_format_check),
        ("Security Scan", run_security_scan),
        ("Standalone Build Test", run_build_test),
    ]
    
    # Skip UI tests on non-Windows systems
    if os.name == 'nt':  # Windows
        tests.insert(2, ("UI Tests", run_ui_tests))
    
    results = {}
    
    for test_name, test_func in tests:
        print(f"\n📋 {test_name}")
        results[test_name] = test_func()
    
    # Print summary
    print(f"\n{'='*60}")
    print("📊 TEST SUMMARY")
    print(f"{'='*60}")
    
    passed = 0
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed!")
        return True
    else:
        print("⚠️  Some tests failed. Please check the output above.")
        return False


def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="HTML to DOCX Converter Test Runner")
    parser.add_argument("--unit", action="store_true", help="Run unit tests only")
    parser.add_argument("--ui", action="store_true", help="Run UI tests only")
    parser.add_argument("--integration", action="store_true", help="Run integration tests only")
    parser.add_argument("--lint", action="store_true", help="Run linting only")
    parser.add_argument("--format", action="store_true", help="Run format check only")
    parser.add_argument("--security", action="store_true", help="Run security scan only")
    parser.add_argument("--build", action="store_true", help="Test standalone build only")
    parser.add_argument("--all", action="store_true", help="Run all tests (default)")
    
    args = parser.parse_args()
    
    # If no specific test is specified, run all
    if not any([args.unit, args.ui, args.integration, args.lint, args.format, args.security, args.build]):
        args.all = True
    
    if args.all:
        success = run_all_tests()
        sys.exit(0 if success else 1)
    
    if args.unit:
        success = run_unit_tests()
        sys.exit(0 if success else 1)
    
    if args.ui:
        success = run_ui_tests()
        sys.exit(0 if success else 1)
    
    if args.integration:
        success = run_integration_tests()
        sys.exit(0 if success else 1)
    
    if args.lint:
        success = run_linting()
        sys.exit(0 if success else 1)
    
    if args.format:
        success = run_format_check()
        sys.exit(0 if success else 1)
    
    if args.security:
        success = run_security_scan()
        sys.exit(0 if success else 1)
    
    if args.build:
        success = run_build_test()
        sys.exit(0 if success else 1)


if __name__ == "__main__":
    main() 