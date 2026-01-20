@echo off
echo ========================================
echo GitHub Push Script for Mental Health Predictor
echo ========================================
echo.

REM Navigate to the script's directory
cd /d "%~dp0"

echo Step 1: Checking Git installation...
git --version
if errorlevel 1 (
    echo ERROR: Git is not installed!
    echo Please install Git from https://git-scm.com/downloads
    pause
    exit /b 1
)
echo.

echo Step 2: Initializing Git repository (if needed)...
if not exist .git (
    git init
    echo Git repository initialized.
) else (
    echo Git repository already exists.
)
echo.

echo Step 3: Checking current status...
git status
echo.

echo Step 4: Adding all files...
git add .
echo.

echo Step 5: Making initial commit...
git commit -m "Initial commit: Mental Health Predictor Flask app"
if errorlevel 1 (
    echo WARNING: Commit failed. This might be because there are no changes.
    echo Continuing anyway...
)
echo.

echo ========================================
echo IMPORTANT: Next Steps
echo ========================================
echo.
echo 1. Go to https://github.com and create a new repository
echo 2. Copy the repository URL (e.g., https://github.com/YOUR_USERNAME/mental-health-predictor.git)
echo 3. Run these commands (replace YOUR_USERNAME and REPO_NAME):
echo.
echo    git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
echo    git branch -M main
echo    git push -u origin main
echo.
echo ========================================
pause
