@echo off
REM Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python to continue.
    exit /b
)

REM Install dependencies (assuming requirements.txt exists)
pip install -r requirements.txt

REM Start main.py in a separate command window and exit
start "" python3 main.py

REM Exit this batch script (close this command prompt window)
exit /b
