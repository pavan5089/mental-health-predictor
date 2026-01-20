# ⚡ Render Quick Start - 5 Minutes

## Fastest Way to Deploy on Render

---

## ✅ CHECKLIST (Before Starting)

- [ ] Code is pushed to GitHub
- [ ] GitHub repository is public (or Render has access)
- [ ] You have a GitHub account

---

## 🚀 5-MINUTE DEPLOYMENT

### 1️⃣ Sign Up (1 minute)
- Go to: **https://render.com**
- Click **"Get Started for Free"**
- Sign up with **GitHub** (easiest!)

### 2️⃣ Create Web Service (2 minutes)
- Click **"New +"** → **"Web Service"**
- Select your repository: `mental-health-predictor`
- Click **"Connect"**

### 3️⃣ Configure (1 minute)
Fill in:
- **Name**: `mental-health-predictor`
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`
- **Plan**: `Free`

### 4️⃣ Add Secret Key (1 minute)
- Scroll to **"Environment Variables"**
- Click **"Add Environment Variable"**
- **Key**: `SECRET_KEY`
- **Value**: Generate with:
  ```bash
  python -c "import secrets; print(secrets.token_hex(32))"
  ```
- Paste the generated key

### 5️⃣ Deploy (Wait 5-10 minutes)
- Click **"Create Web Service"**
- Watch the build logs
- Wait for **"Your service is live"** ✅

---

## 🎉 DONE!

Your app is live at:
```
https://mental-health-predictor.onrender.com
```

---

## 📋 QUICK COMMANDS

### Generate Secret Key:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### Update Your App:
```bash
git add .
git commit -m "Update"
git push origin main
```
(Render auto-deploys!)

---

## ❓ TROUBLESHOOTING

**Build fails?**
→ Check "Logs" tab for errors
→ Make sure all files are in GitHub

**App crashes?**
→ Check `SECRET_KEY` is set
→ View logs for Python errors

**Need help?**
→ Read full guide: `RENDER_DEPLOY.md`

---

**That's it! Your app is live! 🚀**
