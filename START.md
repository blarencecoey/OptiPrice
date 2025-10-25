# Starting the Application

## ✅ Backend is Already Running!

The Python Flask backend is running at: **http://localhost:5000**

The API health check passed! ✓

---

## 🚀 Next Step: Start the Frontend

Open a **NEW terminal window** and run:

```bash
cd "Options Pricing Project"
npm run dev
```

Then open your browser to: **http://localhost:3000**

---

## 📋 Full Instructions

### Every Time You Want to Start the Application:

#### **Terminal 1: Backend Server**

```bash
# Navigate to project
cd "Options Pricing Project"

# Activate virtual environment
source venv/bin/activate       # Linux/Mac
# OR
venv\Scripts\activate          # Windows

# Start backend
cd backend/api
python3 app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

#### **Terminal 2: Frontend Server**

```bash
# Navigate to project
cd "Options Pricing Project"

# Start frontend
npm run dev
```

You should see:
```
ready - started server on 0.0.0.0:3000
```

---

## 🌐 Access the Application

Once both servers are running:

1. Open your browser
2. Navigate to: **http://localhost:3000**
3. You'll see the Options Pricing Calculator!

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
