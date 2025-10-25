# OptiPrice - Startup Guide

This guide helps you start OptiPrice after initial installation.

## Quick Start Commands

### Terminal 1: Backend Server

```bash
cd OptiPrice

# Activate virtual environment
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows

# Start backend
cd backend/api
python3 app.py
```

**Expected output:**
```
 * Running on http://127.0.0.1:5000
 * Running on http://0.0.0.0:5000
```

### Terminal 2: Frontend Server

```bash
cd OptiPrice

# Start frontend
npm run dev
```

**Expected output:**
```
▲ Next.js 14.0.0
- Local:        http://localhost:3000
- ready started server on 0.0.0.0:3000
```

## Access the Application

Open your browser and navigate to:

**http://localhost:3000**

You should see the OptiPrice dashboard!

---

## 🎯 Quick Test

Try this to verify everything works:

1. Go to the **Calculator** tab
2. Keep the default values:
   - Spot Price: 100
   - Strike Price: 100
   - Time to Maturity: 1
   - Risk-Free Rate: 0.05
   - Volatility: 0.2
3. Click **"Calculate Price"**
4. You should see the option price and Greeks!

---

## 🛑 Stopping the Servers

In each terminal, press: **Ctrl+C**

---

## ❓ Common Issues

### "Module not found" Error

**Problem:** Virtual environment not activated

**Solution:**
```bash
source venv/bin/activate       # Linux/Mac
# OR
venv\Scripts\activate          # Windows
```

### "Port already in use" Error

**Problem:** Server already running or port blocked

**Solution:**
1. Stop the existing process
2. Or change the port in configuration

### More Help

See **TROUBLESHOOTING.md** for detailed solutions.

---

## 📱 What You Can Do

- **Calculator Tab**: Price options with different models
- **Comparison Tab**: Compare all three pricing models
- **Visualization Tab**: Generate beautiful charts

Enjoy exploring options pricing! 🎉
