# 🚀 Push Your Code to GitHub - Step by Step

## Quick Method: Use the Batch Script

1. **Double-click** `PUSH_TO_GITHUB.bat` file
2. Follow the instructions it shows

---

## Manual Method: Follow These Steps

### Step 1: Open Command Prompt in Your Project Folder

1. Navigate to: `C:\Users\pavan\OneDrive\Desktop\finalproject\MentalHealthPrediction`
2. Right-click in the folder → "Open in Terminal" or "Open PowerShell here"
3. Or press `Shift + Right-click` → "Open PowerShell window here"

---

### Step 2: Initialize Git (First Time Only)

```bash
git init
```

---

### Step 3: Check What Will Be Added

```bash
git status
```

You should see your project files listed. Make sure no sensitive files (like .db files) are shown.

---

### Step 4: Add All Files

```bash
git add .
```

This adds all files to be committed (respects .gitignore).

---

### Step 5: Make Your First Commit

```bash
git commit -m "Initial commit: Mental Health Predictor Flask app"
```

---

### Step 6: Create GitHub Repository

1. **Go to GitHub**: https://github.com
2. **Click** the **"+"** icon (top right corner)
3. **Select** "New repository"
4. **Repository name**: `mental-health-predictor` (or your choice)
5. **Description**: "Flask Mental Health Prediction Application"
6. **Choose**: Public or Private
7. **IMPORTANT**: Do NOT check "Initialize with README"
8. **Click** "Create repository"

---

### Step 7: Connect and Push to GitHub

After creating the repository, GitHub will show you commands. Use these:

**Replace `YOUR_USERNAME` with your actual GitHub username!**

```bash
# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/mental-health-predictor.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

---

### Step 8: Authentication

When you run `git push`, you'll be asked for credentials:

**Username**: Your GitHub username  
**Password**: Use a **Personal Access Token** (not your GitHub password)

#### How to Get Personal Access Token:

1. Go to GitHub → Click your profile picture (top right)
2. Click **Settings**
3. Scroll down → Click **Developer settings**
4. Click **Personal access tokens** → **Tokens (classic)**
5. Click **Generate new token (classic)**
6. **Note**: Give it a name like "My Computer"
7. **Expiration**: Choose how long (90 days recommended)
8. **Select scopes**: Check **`repo`** (this gives full repository access)
9. Scroll down → Click **Generate token**
10. **COPY THE TOKEN** (you won't see it again!)
11. When prompted for password, **paste this token**

---

## Complete Command Sequence (Copy All at Once)

```bash
# Navigate to project (if not already there)
cd C:\Users\pavan\OneDrive\Desktop\finalproject\MentalHealthPrediction

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Mental Health Predictor Flask app"

# Add remote (REPLACE YOUR_USERNAME and REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/mental-health-predictor.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## Verify Your Push

1. Go to your GitHub repository page
2. You should see all your files:
   - ✅ app.py
   - ✅ models.py
   - ✅ requirements.txt
   - ✅ Procfile
   - ✅ templates/ folder
   - ✅ static/ folder
   - ✅ model/ folder
   - ✅ .gitignore

---

## Troubleshooting

### Error: "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/mental-health-predictor.git
```

### Error: "authentication failed"
- Make sure you're using Personal Access Token, not password
- Token must have `repo` scope checked

### Error: "failed to push some refs"
```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

### Error: "nothing to commit"
- This is normal if you already committed
- Just proceed to push step

---

## What Files Should Be on GitHub?

✅ **Should be there:**
- app.py
- models.py
- requirements.txt
- Procfile
- templates/
- static/
- model/ (with .pkl files)
- .gitignore

❌ **Should NOT be there:**
- instance/ (database files)
- __pycache__/
- venv/
- .db files
- .env files

---

## Next Steps After Push

✅ Code is on GitHub  
✅ Ready to deploy to Render/Railway  
📖 Follow `DEPLOY_STEPS.md` for deployment instructions

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

# View remotes
git remote -v
```

---

**Your code is now ready to push to GitHub! 🎉**
