@echo off
setlocal enabledelayedexpansion

REM Extensive UI Test Runner for HTML to DOCX Converter
REM Runs comprehensive UI tests with multiple browsers and scenarios

echo.
echo ========================================
echo    EXTENSIVE UI TEST RUNNER
echo ========================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.9+ and try again
    pause
    exit /b 1
)

REM Check if required packages are installed
echo Checking dependencies...
python -c "import selenium, pytest, beautifulsoup4, docx" >nul 2>&1
if errorlevel 1 (
    echo Installing required packages...
    pip install selenium pytest pytest-html pytest-xdist
    pip install beautifulsoup4 python-docx lxml
    pip install webdriver-manager
    echo.
)

REM Create reports directory
if not exist "reports" mkdir reports

REM Parse command line arguments
set TEST_TYPE=all
set BROWSERS=chrome,firefox
set PARALLEL=false
set OUTPUT=test-results.json

:parse_args
if "%1"=="" goto :run_tests
if /i "%1"=="--test-type" (
    set TEST_TYPE=%2
    shift
    shift
    goto :parse_args
)
if /i "%1"=="--browsers" (
    set BROWSERS=%2
    shift
    shift
    goto :parse_args
)
if /i "%1"=="--parallel" (
    set PARALLEL=true
    shift
    goto :parse_args
)
if /i "%1"=="--output" (
    set OUTPUT=%2
    shift
    shift
    goto :parse_args
)
if /i "%1"=="--help" goto :show_help
shift
goto :parse_args

:show_help
echo Usage: run_extensive_ui_tests.bat [options]
echo.
echo Options:
echo   --test-type TYPE    Test type: all, basic, complex, responsive, typography, tables, accessibility, performance, cross-browser
echo   --browsers LIST     Comma-separated list of browsers: chrome, firefox, edge
echo   --parallel          Run tests in parallel
echo   --output FILE       Output file for test results (default: test-results.json)
echo   --help              Show this help message
echo.
echo Examples:
echo   run_extensive_ui_tests.bat
echo   run_extensive_ui_tests.bat --test-type basic --browsers chrome
echo   run_extensive_ui_tests.bat --test-type all --browsers chrome,firefox --parallel
echo.
pause
exit /b 0

:run_tests
echo Test Configuration:
echo   Test Type: %TEST_TYPE%
echo   Browsers: %BROWSERS%
echo   Parallel: %PARALLEL%
echo   Output: %OUTPUT%
echo.

REM Run the test runner
echo Starting extensive UI tests...
python run_extensive_ui_tests.py --test-type %TEST_TYPE% --browsers %BROWSERS% --output %OUTPUT%

if "%PARALLEL%"=="true" (
    echo Running tests in parallel mode...
    python run_extensive_ui_tests.py --test-type %TEST_TYPE% --browsers %BROWSERS% --parallel --output %OUTPUT%
) else (
    echo Running tests sequentially...
    python run_extensive_ui_tests.py --test-type %TEST_TYPE% --browsers %BROWSERS% --output %OUTPUT%
)

REM Check if tests completed successfully
if errorlevel 1 (
    echo.
    echo ========================================
    echo    SOME TESTS FAILED
    echo ========================================
    echo.
    echo Check the test reports in the 'reports' directory for details
    echo.
    pause
    exit /b 1
) else (
    echo.
    echo ========================================
    echo    ALL TESTS PASSED
    echo ========================================
    echo.
    echo Test results saved to: %OUTPUT%
    echo Test reports available in: reports\
    echo.
)

REM Open reports directory
echo Opening reports directory...
start reports

pause 