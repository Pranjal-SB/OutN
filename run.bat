@echo off
REM Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python to continue.
    exit /b
)

REM Install dependencies
pip install -r requirements.txt

REM Start main.py in a separate command window and exit
start "" python main.py

REM Exit this batch script (close this command prompt window)
exit /b
