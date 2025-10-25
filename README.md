# Options Pricing Models Web Application

A comprehensive options pricing web application featuring Black-Scholes, Binomial Tree, and Monte Carlo methods with advanced data visualization and analysis tools. Built with Python (Flask) backend and Next.js frontend.

![Options Pricing Dashboard](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Next.js](https://img.shields.io/badge/Next.js-14.0-black.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

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

## Project Structure

```
Options Pricing Project/
├── backend/                    # Python Flask backend
│   ├── models/                # Pricing models
│   │   ├── black_scholes.py  # Black-Scholes implementation
│   │   ├── binomial_tree.py  # Binomial Tree implementation
│   │   └── monte_carlo.py    # Monte Carlo implementation
│   ├── utils/                 # Utilities
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
├── package.json              # Node.js dependencies
├── next.config.js            # Next.js configuration
├── tsconfig.json             # TypeScript configuration
└── tailwind.config.js        # Tailwind CSS configuration
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Node.js 18.0 or higher
- npm or yarn package manager

### Backend Setup

1. Navigate to the project directory:
```bash
cd "Options Pricing Project"
```

2. Create a Python virtual environment:
```bash
python3 -m venv venv

# On Windows
venv\Scripts\activate

# On Linux/Mac
source venv/bin/activate
```

3. Install Python dependencies:
```bash
cd backend
pip install -r requirements.txt
```

4. Start the Flask backend server:
```bash
cd api
python3 app.py
```

The backend API will run on `http://localhost:5000`

### Frontend Setup

1. Open a new terminal and navigate to the project directory:
```bash
cd "Options Pricing Project"
```

2. Install Node.js dependencies:
```bash
npm install
```

3. Start the Next.js development server:
```bash
npm run dev
```

The frontend will run on `http://localhost:3000`

4. Open your browser and navigate to `http://localhost:3000`

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
cd backend/api
gunicorn app:app
```

**Frontend:**
```bash
npm run build
npm start
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
