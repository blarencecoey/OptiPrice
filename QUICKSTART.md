# OptiPrice - Quick Start Guide

Get up and running with OptiPrice in **5 minutes**!

## Prerequisites

Ensure you have:
- Python 3.8+ installed
- Node.js 18.0+ installed
- Git installed

## Installation

### Step 1: Clone & Navigate

```bash
git clone https://github.com/blarencecoey/OptiPrice.git
cd OptiPrice
```

### Step 2: Backend Setup (2 minutes)

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r backend/requirements.txt
```

### Step 3: Frontend Setup (2 minutes)

Open a **new terminal** window:

```bash
cd OptiPrice
npm install
```

## Running the Application

### Terminal 1 - Backend Server

```bash
# Activate venv (if not already activated)
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Navigate and start
cd backend/api
python3 app.py
```

✅ Backend running at: **http://localhost:5000**

### Terminal 2 - Frontend Server

```bash
# From project root
npm run dev
```

✅ Frontend running at: **http://localhost:3000**

## First Steps

1. Open your browser to http://localhost:3000
2. Try the **Calculator** tab:
   - Keep default values (Spot: 100, Strike: 100, etc.)
   - Click "Calculate Price"
   - See the option price and Greeks

3. Try the **Comparison** tab:
   - Click "Compare All Models"
   - See how different models price the same option

4. Try the **Visualization** tab:
   - Select "Option Price vs Spot Price"
   - Click "Generate Visualization"
   - See a beautiful chart!

## Example API Usage

### Price an Option (cURL)
```bash
curl -X POST http://localhost:5000/api/price/black-scholes \
  -H "Content-Type: application/json" \
  -d '{
    "spotPrice": 100,
    "strikePrice": 100,
    "timeToMaturity": 1,
    "riskFreeRate": 0.05,
    "volatility": 0.2,
    "optionType": "call"
  }'
```

### Response
```json
{
  "price": 10.4506,
  "greeks": {
    "delta": 0.6368,
    "gamma": 0.0188,
    "vega": 0.3752,
    "theta": -0.0182,
    "rho": 0.5320
  }
}
```

## Common Issues

### Issue: Port already in use
**Solution:** Change ports in the configuration
- Backend: Edit `backend/api/app.py`, change `port=5000`
- Frontend: Edit `next.config.js`, update the proxy destination

### Issue: Module not found
**Solution:** Make sure you activated the virtual environment and installed dependencies

### Issue: CORS errors
**Solution:** Ensure both backend and frontend are running

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Explore the API endpoints
- Try different option parameters
- Experiment with visualizations

## Support

If you encounter issues:
1. Check both terminals for error messages
2. Verify all dependencies are installed
3. Ensure you're using Python 3.8+ and Node.js 18+
4. Open an issue on GitHub
