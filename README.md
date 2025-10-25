# OptiPrice - Options Pricing Models Web Application

A comprehensive, full-stack options pricing web application featuring Black-Scholes, Binomial Tree, and Monte Carlo methods with advanced data visualization and analysis tools. Built with Python (Flask) backend and Next.js frontend.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Next.js](https://img.shields.io/badge/Next.js-14.0-black.svg)](https://nextjs.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3-lightgrey.svg)](https://flask.palletsprojects.com/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue.svg)](https://www.typescriptlang.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-endpoints)
- [Technical Details](#technical-details)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Features

### Pricing Models
- **Black-Scholes Model**: Closed-form solution for European options with complete Greeks calculations
- **Binomial Tree Model**: Flexible lattice-based pricing supporting both European and American options
- **Monte Carlo Simulation**: Stochastic pricing with confidence intervals and path visualization

### Advanced Analytics
- **Greeks Calculation**: Delta, Gamma, Vega, Theta, and Rho for risk management
- **Model Comparison**: Side-by-side comparison of all three pricing models
- **Implied Volatility**: Calculate market-implied volatility from option prices
- **Sensitivity Analysis**: Analyze how option prices respond to parameter changes
- **Payoff Diagrams**: Visualize profit/loss for different option strategies

### Interactive Visualizations
- Option price vs spot price curves
- Greeks surface plots
- Monte Carlo simulation paths
- Volatility surfaces
- Real-time chart generation

## Demo

> **Note:** Add screenshots or GIF demonstrations here once deployed

### Live Features:
- Real-time option pricing calculations
- Interactive parameter inputs with validation
- Responsive design for desktop and mobile
- Beautiful data visualizations with Matplotlib
- REST API for integration with other applications

## Quick Start

Get up and running in 5 minutes! See [QUICKSTART.md](QUICKSTART.md) for detailed instructions.

```bash
# 1. Clone the repository
git clone https://github.com/blarencecoey/OptiPrice.git
cd OptiPrice

# 2. Backend setup
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r backend/requirements.txt

# 3. Frontend setup (in a new terminal)
npm install

# 4. Run the application
# Terminal 1 - Backend
cd backend/api && python3 app.py

# Terminal 2 - Frontend
npm run dev

# 5. Open http://localhost:3000 in your browser
```

## Project Structure

```
OptiPrice/
├── backend/                    # Python Flask backend
│   ├── __init__.py            # Package initialization
│   ├── models/                # Pricing models
│   │   ├── __init__.py       # Models package
│   │   ├── black_scholes.py  # Black-Scholes implementation
│   │   ├── binomial_tree.py  # Binomial Tree implementation
│   │   └── monte_carlo.py    # Monte Carlo implementation
│   ├── utils/                 # Utilities
│   │   ├── __init__.py       # Utils package
│   │   ├── visualizer.py     # Chart generation
│   │   └── analyzer.py       # Analysis tools
│   ├── api/                   # API endpoints
│   │   └── app.py            # Flask application
│   └── requirements.txt       # Python dependencies
├── app/                       # Next.js app directory
│   ├── page.tsx              # Main page
│   ├── layout.tsx            # Layout component
│   └── globals.css           # Global styles
├── components/                # React components
│   ├── OptionsCalculator.tsx # Pricing calculator
│   ├── ComparisonView.tsx    # Model comparison
│   └── VisualizationPanel.tsx # Visualization interface
├── lib/                       # Utilities
│   └── api.ts                # API client
├── venv/                      # Python virtual environment (local only)
├── package.json              # Node.js dependencies
├── next.config.js            # Next.js configuration
├── tsconfig.json             # TypeScript configuration
├── tailwind.config.js        # Tailwind CSS configuration
├── README.md                 # Project documentation
├── QUICKSTART.md             # Quick start guide
└── START.md                  # Startup instructions
```

## Installation

### Prerequisites

- **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- **Node.js 18.0+** - [Download Node.js](https://nodejs.org/)
- **npm or yarn** - Package manager (comes with Node.js)
- **Git** - [Download Git](https://git-scm.com/downloads)

### Step 1: Clone the Repository

```bash
git clone https://github.com/blarencecoey/OptiPrice.git
cd OptiPrice
```

### Step 2: Backend Setup

```bash
# Create a Python virtual environment
python3 -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install Python dependencies
cd backend
pip install -r requirements.txt
cd ..
```

**Verify backend installation:**
```bash
python3 -c "import sys; sys.path.insert(0, 'backend'); from models import BlackScholesModel; print('✓ Backend installation successful!')"
```

### Step 3: Frontend Setup

Open a **new terminal** window:

```bash
cd OptiPrice

# Install Node.js dependencies
npm install
```

**Verify frontend installation:**
```bash
npm run build
```

### Step 4: Run the Application

**Terminal 1 - Start Backend Server:**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Navigate to API directory
cd backend/api

# Start Flask server
python3 app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Running on http://0.0.0.0:5000
```

**Terminal 2 - Start Frontend Server:**
```bash
# From project root
npm run dev
```

You should see:
```
▲ Next.js 14.0.0
- Local:        http://localhost:3000
- ready started server on 0.0.0.0:3000
```

### Step 5: Access the Application

Open your browser and navigate to:
```
http://localhost:3000
```

You should see the OptiPrice dashboard!

## Usage

### Options Calculator

1. Select a pricing model (Black-Scholes, Binomial Tree, or Monte Carlo)
2. Choose option type (Call or Put)
3. Enter option parameters:
   - Spot Price (S): Current price of the underlying asset
   - Strike Price (K): Exercise price of the option
   - Time to Maturity (T): Time until expiration in years
   - Risk-Free Rate (r): Annual risk-free interest rate
   - Volatility (σ): Annual volatility of the underlying asset
4. Click "Calculate Price" to get the option price and Greeks

### Model Comparison

1. Enter option parameters
2. Click "Compare All Models" to see results from all three pricing methods
3. Compare prices and Greeks across different models

### Visualization

1. Select visualization type:
   - **Price vs Spot**: Shows how option price changes with underlying price
   - **Greeks**: Displays all Greeks across different spot prices
   - **Monte Carlo Paths**: Shows simulated price paths
2. Configure parameters
3. Click "Generate Visualization" to create charts

## API Endpoints

### Pricing Endpoints

- `POST /api/price/black-scholes` - Price option using Black-Scholes
- `POST /api/price/binomial-tree` - Price option using Binomial Tree
- `POST /api/price/monte-carlo` - Price option using Monte Carlo
- `POST /api/compare` - Compare all pricing models

### Visualization Endpoints

- `POST /api/visualize/price-vs-spot` - Generate price vs spot chart
- `POST /api/visualize/greeks` - Generate Greeks charts
- `POST /api/visualize/monte-carlo-paths` - Generate Monte Carlo paths chart

### Analysis Endpoints

- `POST /api/analyze/payoff` - Calculate payoff diagram
- `POST /api/analyze/sensitivity` - Perform sensitivity analysis
- `POST /api/implied-volatility` - Calculate implied volatility
- `GET /api/health` - Health check endpoint

## Technical Details

### Black-Scholes Model

The Black-Scholes model calculates European option prices using the closed-form formula:

**Call Option:**
```
C = S₀N(d₁) - Ke^(-rT)N(d₂)
```

**Put Option:**
```
P = Ke^(-rT)N(-d₂) - S₀N(-d₁)
```

Where:
- d₁ = [ln(S₀/K) + (r + σ²/2)T] / (σ√T)
- d₂ = d₁ - σ√T

### Binomial Tree Model

Uses a discrete-time lattice to model the underlying asset price evolution:
- Up factor: u = e^(σ√Δt)
- Down factor: d = 1/u
- Risk-neutral probability: p = (e^(rΔt) - d) / (u - d)

Supports both European and American exercise styles.

### Monte Carlo Simulation

Simulates the underlying asset price using Geometric Brownian Motion:
```
S(t) = S₀ exp[(r - σ²/2)t + σW(t)]
```

Where W(t) is a Wiener process. Provides confidence intervals based on simulation results.

## Technologies Used

### Backend
- **Python 3.8+**: Core language
- **Flask**: Web framework
- **NumPy**: Numerical computations
- **SciPy**: Statistical functions
- **Pandas**: Data manipulation
- **Matplotlib**: Chart generation

### Frontend
- **Next.js 14**: React framework
- **TypeScript**: Type-safe JavaScript
- **Tailwind CSS**: Styling
- **Axios**: HTTP client

## Troubleshooting

### Common Issues and Solutions

#### 1. "attempted relative import beyond top-level package" Error

**Problem:** This error occurs when trying to import models in the analyzer or visualizer.

**Solution:** The project includes `__init__.py` files in the backend directory structure. Ensure these files exist:
- `backend/__init__.py`
- `backend/models/__init__.py`
- `backend/utils/__init__.py`

The imports in `backend/utils/analyzer.py` use a try-except pattern to handle both relative and absolute imports:
```python
try:
    from ..models import BlackScholesModel, BinomialTreeModel, MonteCarloModel
except (ImportError, ValueError):
    from models import BlackScholesModel, BinomialTreeModel, MonteCarloModel
```

#### 2. "Module not found" Error

**Problem:** Python can't find the required modules.

**Solution:**
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # Linux/Mac
# OR
venv\Scripts\activate     # Windows

# Reinstall dependencies
cd backend
pip install -r requirements.txt
```

#### 3. "Port already in use" Error

**Problem:** Port 5000 or 3000 is already occupied.

**Solution:**
```bash
# Find and kill the process (Linux/Mac)
lsof -ti:5000 | xargs kill -9  # Backend
lsof -ti:3000 | xargs kill -9  # Frontend

# On Windows, use Task Manager or:
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

Or change the ports:
- **Backend:** Edit `backend/api/app.py`, change `port=5000` to another port
- **Frontend:** Create `.env.local` and add `PORT=3001`

#### 4. CORS Errors

**Problem:** Cross-Origin Resource Sharing errors in browser console.

**Solution:** Ensure both servers are running:
- Backend: `http://localhost:5000`
- Frontend: `http://localhost:3000`

The Flask app has CORS enabled via `flask-cors`.

#### 5. Import Errors with NumPy/SciPy

**Problem:** Errors related to NumPy or SciPy installation on Apple Silicon or Windows.

**Solution:**
```bash
# For Apple Silicon (M1/M2)
pip install --upgrade pip
pip install numpy scipy --no-cache-dir

# For Windows
pip install --upgrade pip setuptools wheel
pip install numpy scipy
```

#### 6. Frontend Build Errors

**Problem:** TypeScript or build errors in Next.js.

**Solution:**
```bash
# Clear Next.js cache
rm -rf .next
npm run dev
```

#### 7. Flask App Not Starting

**Problem:** Flask server won't start or crashes immediately.

**Solution:**
```bash
# Verify Python version
python3 --version  # Should be 3.8+

# Test imports manually
cd backend/api
python3 -c "from app import app; print('Flask app loaded successfully')"
```

### Still Having Issues?

1. Check both terminal windows for error messages
2. Verify all prerequisites are installed:
   ```bash
   python3 --version
   node --version
   npm --version
   ```
3. Review the [QUICKSTART.md](QUICKSTART.md) guide
4. Open an issue on [GitHub](https://github.com/blarencecoey/OptiPrice/issues)

## Development

### Running Tests

```bash
# Backend tests (to be implemented)
cd backend
python -m pytest

# Frontend tests (to be implemented)
npm test
```

### Building for Production

**Backend:**
```bash
# Install production WSGI server
pip install gunicorn

# Run with gunicorn
cd backend/api
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

**Frontend:**
```bash
# Build optimized production bundle
npm run build

# Start production server
npm start
```

### Environment Variables

Create a `.env.local` file in the project root for frontend configuration:
```bash
NEXT_PUBLIC_API_URL=http://localhost:5000
```

For backend, create `backend/.env`:
```bash
FLASK_ENV=development
FLASK_DEBUG=1
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Black-Scholes model based on the seminal work by Fischer Black, Myron Scholes, and Robert Merton
- Binomial model based on Cox-Ross-Rubinstein framework
- Monte Carlo methods for financial applications

## Future Enhancements

- [ ] Add support for exotic options (Asian, Barrier, Lookback)
- [ ] Implement real-time market data integration
- [ ] Add portfolio optimization tools
- [ ] Support for option strategies (spreads, straddles, etc.)
- [ ] Historical volatility calculation
- [ ] Integration with financial data APIs
- [ ] User authentication and saved portfolios
- [ ] Mobile-responsive improvements

## Contact

For questions or feedback, please open an issue on GitHub.

---

**Note**: This application is for educational purposes. Always consult with financial professionals before making investment decisions.
