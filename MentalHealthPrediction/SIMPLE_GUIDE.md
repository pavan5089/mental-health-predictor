# 📖 Simple Guide: Push Your Code to GitHub

## What You Need to Do (Step by Step)

---

## PART 1: Create GitHub Account & Repository

### Step 1: Create GitHub Account (if you don't have one)
1. Go to: **https://github.com**
2. Click **"Sign up"**
3. Enter your email, password, and username
4. Verify your email

### Step 2: Create a New Repository
1. After logging in, click the **"+"** button (top right corner)
2. Click **"New repository"**
3. Fill in:
   - **Repository name**: `mental-health-predictor` (or any name you like)
   - **Description**: "My Mental Health Prediction App" (optional)
   - **Public** or **Private** (your choice)
   - **IMPORTANT**: Do NOT check "Add a README file"
4. Click **"Create repository"**

---

## PART 2: Get Personal Access Token (For Authentication)

### Why? GitHub doesn't accept passwords anymore, you need a token.

1. On GitHub, click your **profile picture** (top right)
2. Click **"Settings"**
3. Scroll down → Click **"Developer settings"** (left sidebar)
4. Click **"Personal access tokens"** → **"Tokens (classic)"**
5. Click **"Generate new token"** → **"Generate new token (classic)"**
6. Fill in:
   - **Note**: Type "My Computer" or "Laptop"
   - **Expiration**: Choose "90 days" (or longer)
   - **Select scopes**: Check the box **"repo"** (this gives full access)
7. Scroll down → Click **"Generate token"**
8. **COPY THE TOKEN** (it looks like: `ghp_xxxxxxxxxxxxxxxxxxxx`)
   - ⚠️ **Save it somewhere safe!** You won't see it again!

---

## PART 3: Push Your Code to GitHub

### Method 1: Using Command Prompt (Recommended)

1. **Open Command Prompt or PowerShell**
   - Press `Windows + R`
   - Type `cmd` and press Enter
   - OR right-click in your project folder → "Open in Terminal"

2. **Navigate to your project folder:**
   ```bash
   cd C:\Users\pavan\OneDrive\Desktop\finalproject\MentalHealthPrediction
   ```

3. **Run these commands one by one:**

   ```bash
   # Initialize git (first time only)
   git init
   ```

   ```bash
   # Add all your files
   git add .
   ```

   ```bash
   # Save your files (commit)
   git commit -m "First commit: Mental Health Predictor"
   ```

   ```bash
   # Connect to your GitHub repository
   # REPLACE YOUR_USERNAME with your actual GitHub username!
   git remote add origin https://github.com/YOUR_USERNAME/mental-health-predictor.git
   ```
   
   **Example**: If your username is `john123`, the command would be:
   ```bash
   git remote add origin https://github.com/john123/mental-health-predictor.git
   ```

   ```bash
   # Rename branch to main
   git branch -M main
   ```

   ```bash
   # Push to GitHub
   git push -u origin main
   ```

4. **When asked for credentials:**
   - **Username**: Your GitHub username
   - **Password**: Paste the Personal Access Token you copied earlier (NOT your GitHub password!)

5. **Wait for upload to complete** (may take 1-2 minutes)

---

### Method 2: Using the Batch File (Easier)

1. **Double-click** the file: `PUSH_TO_GITHUB.bat`
2. It will run the git commands automatically
3. When it asks you to add the remote, follow the instructions it shows
4. Use your Personal Access Token when prompted

---

## PART 4: Verify It Worked

1. Go to your GitHub repository page:
   - `https://github.com/YOUR_USERNAME/mental-health-predictor`
2. You should see all your files:
   - ✅ app.py
   - ✅ models.py
   - ✅ requirements.txt
   - ✅ templates/ folder
   - ✅ static/ folder
   - ✅ model/ folder

**If you see your files, you're done! 🎉**

---

## Visual Summary

```
1. Create GitHub Account
   ↓
2. Create Repository on GitHub
   ↓
3. Get Personal Access Token
   ↓
4. Open Command Prompt in your project folder
   ↓
5. Run: git init
   ↓
6. Run: git add .
   ↓
7. Run: git commit -m "First commit"
   ↓
8. Run: git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
   ↓
9. Run: git branch -M main
   ↓
10. Run: git push -u origin main
   ↓
11. Enter username and token when asked
   ↓
✅ Done! Your code is on GitHub!
```

---

## Common Questions

### Q: What if I get "remote origin already exists" error?
**A:** Run this first:
```bash
git remote remove origin
```
Then continue with step 8.

### Q: What if I get "authentication failed"?
**A:** Make sure you're using the Personal Access Token (not your password)

### Q: What if I forget my token?
**A:** Generate a new one (same steps as before)

### Q: Can I skip the token and use password?
**A:** No, GitHub requires tokens for security

### Q: What files will be uploaded?
**A:** All files EXCEPT:
- Database files (.db)
- Python cache (__pycache__)
- Virtual environment (venv/)
- These are excluded by .gitignore

---

## What Happens After Push?

✅ Your code is now on GitHub  
✅ You can access it from anywhere  
✅ You can share it with others  
✅ Ready to deploy to Render/Railway  

---

## Next Step: Deploy Your App

After pushing to GitHub, you can deploy your app:
1. Read `DEPLOY_STEPS.md` file
2. Follow instructions to deploy on Render.com
3. Your app will be live on the internet!

---

## Need Help?

If something doesn't work:
1. Check the error message
2. Make sure you followed all steps
3. Verify your GitHub username is correct
4. Make sure you're using the token (not password)

---

**That's it! Follow these steps and your code will be on GitHub! 🚀**
