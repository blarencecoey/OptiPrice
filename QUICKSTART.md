# Quick Start Guide

## Installation (5 minutes)

### Step 1: Backend Setup

```bash
# Navigate to project
cd "Options Pricing Project"

# Create and activate virtual environment
python3 -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

# Install dependencies
cd backend
pip install -r requirements.txt
```

### Step 2: Frontend Setup

```bash
# In a new terminal, navigate to project
cd "Options Pricing Project"

# Install dependencies
npm install
```

## Running the Application

### Terminal 1 - Backend
```bash
cd "Options Pricing Project/backend/api"
python3 app.py
```
Backend will run on: http://localhost:5000

### Terminal 2 - Frontend
```bash
cd "Options Pricing Project"
npm run dev
```
Frontend will run on: http://localhost:3000

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
