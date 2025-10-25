@echo off
REM Options Pricing Project Setup Script (Windows)
REM This script sets up both backend and frontend environments

echo ========================================
echo Options Pricing Project Setup
echo ========================================
echo.

REM Check Python version
echo Checking Python version...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo X Python not found. Please install Python 3.8 or higher.
    pause
    exit /b 1
)
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo √ Python found: %PYTHON_VERSION%

REM Check Node.js version
echo Checking Node.js version...
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo X Node.js not found. Please install Node.js 18.0 or higher.
    pause
    exit /b 1
)
for /f "tokens=*" %%i in ('node --version') do set NODE_VERSION=%%i
echo √ Node.js found: %NODE_VERSION%

echo.
echo ========================================
echo Setting up Python Backend
echo ========================================

REM Create virtual environment
echo Creating Python virtual environment...
python -m venv venv

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install Python dependencies
echo Installing Python dependencies...
cd backend
pip install --upgrade pip
pip install -r requirements.txt
cd ..

echo √ Backend setup complete!

echo.
echo ========================================
echo Setting up Next.js Frontend
echo ========================================

REM Install Node.js dependencies
echo Installing Node.js dependencies...
npm install

echo √ Frontend setup complete!

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To start the application:
echo.
echo Terminal 1 (Backend):
echo   venv\Scripts\activate
echo   cd backend\api
echo   python app.py
echo.
echo Terminal 2 (Frontend):
echo   npm run dev
echo.
echo Then open http://localhost:3000 in your browser
echo.
pause
