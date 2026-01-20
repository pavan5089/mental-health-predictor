# GitHub Setup Guide - First Time Push

## Step-by-Step Instructions to Push Your Code to GitHub

### Prerequisites
- Git installed on your computer
- GitHub account created

---

## STEP 1: Check if Git is Installed

Open your terminal/command prompt and run:
```bash
git --version
```

If not installed, download from: https://git-scm.com/downloads

---

## STEP 2: Navigate to Your Project Folder

```bash
cd C:\Users\pavan\OneDrive\Desktop\finalproject\MentalHealthPrediction
```

---

## STEP 3: Initialize Git Repository (if not already done)

```bash
git init
```

---

## STEP 4: Check What Files Will Be Added

```bash
git status
```

This shows which files will be committed. Make sure `.gitignore` is working correctly.

---

## STEP 5: Add All Files to Git

```bash
git add .
```

This adds all files (respecting .gitignore rules).

---

## STEP 6: Make Your First Commit

```bash
git commit -m "Initial commit: Mental Health Predictor Flask app"
```

---

## STEP 7: Create GitHub Repository

1. Go to https://github.com
2. Click the **"+"** icon (top right) → **"New repository"**
3. Repository name: `mental-health-predictor` (or your choice)
4. Description: "Flask-based Mental Health Prediction Application"
5. Choose: **Public** (or Private if you prefer)
6. **DO NOT** check "Initialize with README" (we already have files)
7. Click **"Create repository"**

---

## STEP 8: Connect Local Repository to GitHub

After creating the repository, GitHub will show you commands. Use these:

```bash
# Add remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/mental-health-predictor.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

**Replace `YOUR_USERNAME` with your actual GitHub username!**

---

## STEP 9: Verify Push

1. Go to your GitHub repository page
2. You should see all your files there
3. Check that these are present:
   - ✅ app.py
   - ✅ models.py
   - ✅ requirements.txt
   - ✅ Procfile
   - ✅ templates/ folder
   - ✅ static/ folder
   - ✅ model/ folder

---

## Complete Command Sequence (Copy & Paste)

```bash
# Navigate to project
cd C:\Users\pavan\OneDrive\Desktop\finalproject\MentalHealthPrediction

# Initialize git (if first time)
git init

# Check status
git status

# Add all files
git add .

# Commit
git commit -m "Initial commit: Mental Health Predictor Flask app"

# Add remote (REPLACE YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/mental-health-predictor.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## If You Get Authentication Error

GitHub now requires a Personal Access Token instead of password:

1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Name it: "My Computer"
4. Select scopes: Check "repo" (all repo permissions)
5. Click "Generate token"
6. **Copy the token** (you won't see it again!)
7. When prompted for password, paste the token instead

---

## Troubleshooting

### Error: "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/mental-health-predictor.git
```

### Error: "failed to push some refs"
```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

### Error: "authentication failed"
- Use Personal Access Token (see above)
- Or use GitHub Desktop app

---

## Verify Your Push

After successful push, check:
- ✅ All files are on GitHub
- ✅ No sensitive files (like .db files) are visible
- ✅ .gitignore is working

---

## Next Steps After Push

1. ✅ Code is on GitHub
2. ✅ Ready to deploy to Render/Railway
3. ✅ Follow DEPLOY_STEPS.md for deployment

---

## Quick Reference

```bash
# Check status
git status

# Add files
git add .

# Commit
git commit -m "Your message"

# Push
git push origin main

# Pull latest changes
git pull origin main
```

---

**Your code is now on GitHub! 🎉**
