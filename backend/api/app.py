"""Flask API for Options Pricing Application"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Add parent directory to path to import models
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models import BlackScholesModel, BinomialTreeModel, MonteCarloModel
from utils import OptionsVisualizer, OptionsAnalyzer
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for Next.js frontend


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({'status': 'healthy', 'message': 'Options Pricing API is running'})


@app.route('/api/price/black-scholes', methods=['POST'])
def price_black_scholes():
    """Calculate option price using Black-Scholes model."""
    try:
        data = request.json
        model = BlackScholesModel(
            S=float(data['spotPrice']),
            K=float(data['strikePrice']),
            T=float(data['timeToMaturity']),
            r=float(data['riskFreeRate']),
            sigma=float(data['volatility']),
            option_type=data.get('optionType', 'call')
        )

        result = {
            'price': model.price(),
            'greeks': model.greeks()
        }

        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/price/binomial-tree', methods=['POST'])
def price_binomial_tree():
    """Calculate option price using Binomial Tree model."""
    try:
        data = request.json
        model = BinomialTreeModel(
            S=float(data['spotPrice']),
            K=float(data['strikePrice']),
            T=float(data['timeToMaturity']),
            r=float(data['riskFreeRate']),
            sigma=float(data['volatility']),
            steps=int(data.get('steps', 100)),
            option_type=data.get('optionType', 'call'),
            exercise=data.get('exercise', 'european')
        )

        result = {
            'price': model.price(),
            'delta': model.delta(),
            'gamma': model.gamma()
        }

        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/price/monte-carlo', methods=['POST'])
def price_monte_carlo():
    """Calculate option price using Monte Carlo simulation."""
    try:
        data = request.json
        model = MonteCarloModel(
            S=float(data['spotPrice']),
            K=float(data['strikePrice']),
            T=float(data['timeToMaturity']),
            r=float(data['riskFreeRate']),
            sigma=float(data['volatility']),
            simulations=int(data.get('simulations', 10000)),
            option_type=data.get('optionType', 'call'),
            seed=42
        )

        result = model.price_with_confidence()

        return jsonify({
            'price': result['price'],
            'standardError': result['std_error'],
            'confidenceInterval': {
                'lower': result['lower_bound'],
                'upper': result['upper_bound']
            }
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/compare', methods=['POST'])
def compare_models():
    """Compare all pricing models."""
    try:
        data = request.json
        results = OptionsAnalyzer.compare_models(
            S=float(data['spotPrice']),
            K=float(data['strikePrice']),
            T=float(data['timeToMaturity']),
            r=float(data['riskFreeRate']),
            sigma=float(data['volatility']),
            option_type=data.get('optionType', 'call')
        )

        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/visualize/price-vs-spot', methods=['POST'])
def visualize_price_vs_spot():
    """Generate option price vs spot price chart."""
    try:
        data = request.json
        model_map = {
            'black-scholes': BlackScholesModel,
            'binomial-tree': BinomialTreeModel,
            'monte-carlo': MonteCarloModel
        }

        model_class = model_map.get(data['model'])
        if not model_class:
            return jsonify({'error': 'Invalid model type'}), 400

        spot_min = float(data.get('spotMin', data['strikePrice'] * 0.5))
        spot_max = float(data.get('spotMax', data['strikePrice'] * 1.5))

        kwargs = {}
        if data['model'] == 'binomial-tree':
            kwargs['steps'] = int(data.get('steps', 100))
        elif data['model'] == 'monte-carlo':
            kwargs['simulations'] = int(data.get('simulations', 10000))
            kwargs['seed'] = 42

        image_base64 = OptionsVisualizer.plot_option_price_vs_spot(
            model_class=model_class,
            K=float(data['strikePrice']),
            T=float(data['timeToMaturity']),
            r=float(data['riskFreeRate']),
            sigma=float(data['volatility']),
            spot_range=(spot_min, spot_max),
            option_type=data.get('optionType', 'call'),
            **kwargs
        )

        return jsonify({'image': image_base64})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/visualize/greeks', methods=['POST'])
def visualize_greeks():
    """Generate Greeks visualization."""
    try:
        data = request.json

        spot_min = float(data.get('spotMin', data['strikePrice'] * 0.5))
        spot_max = float(data.get('spotMax', data['strikePrice'] * 1.5))

        image_base64 = OptionsVisualizer.plot_greeks(
            model_class=BlackScholesModel,
            K=float(data['strikePrice']),
            T=float(data['timeToMaturity']),
            r=float(data['riskFreeRate']),
            sigma=float(data['volatility']),
            spot_range=(spot_min, spot_max),
            option_type=data.get('optionType', 'call')
        )

        return jsonify({'image': image_base64})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/visualize/monte-carlo-paths', methods=['POST'])
def visualize_monte_carlo():
    """Generate Monte Carlo paths visualization."""
    try:
        data = request.json
        model = MonteCarloModel(
            S=float(data['spotPrice']),
            K=float(data['strikePrice']),
            T=float(data['timeToMaturity']),
            r=float(data['riskFreeRate']),
            sigma=float(data['volatility']),
            option_type=data.get('optionType', 'call'),
            seed=42
        )

        paths = model.get_paths(num_paths=int(data.get('numPaths', 100)))
        image_base64 = OptionsVisualizer.plot_monte_carlo_paths(
            paths=paths,
            K=float(data['strikePrice']),
            option_type=data.get('optionType', 'call')
        )

        return jsonify({'image': image_base64})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/analyze/payoff', methods=['POST'])
def analyze_payoff():
    """Calculate payoff diagram data."""
    try:
        data = request.json
        K = float(data['strikePrice'])
        spot_min = float(data.get('spotMin', K * 0.5))
        spot_max = float(data.get('spotMax', K * 1.5))

        S_range = np.linspace(spot_min, spot_max, 100)

        result = OptionsAnalyzer.payoff_diagram(
            S_range=S_range,
            K=K,
            premium=float(data['premium']),
            option_type=data.get('optionType', 'call'),
            position=data.get('position', 'long')
        )

        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/analyze/sensitivity', methods=['POST'])
def analyze_sensitivity():
    """Perform sensitivity analysis."""
    try:
        data = request.json

        result = OptionsAnalyzer.sensitivity_analysis(
            S=float(data['spotPrice']),
            K=float(data['strikePrice']),
            T=float(data['timeToMaturity']),
            r=float(data['riskFreeRate']),
            sigma=float(data['volatility']),
            option_type=data.get('optionType', 'call'),
            parameter=data['parameter'],
            variation_range=float(data.get('variationRange', 0.2))
        )

        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/implied-volatility', methods=['POST'])
def calculate_implied_volatility():
    """Calculate implied volatility."""
    try:
        data = request.json

        iv = OptionsAnalyzer.calculate_implied_volatility(
            market_price=float(data['marketPrice']),
            S=float(data['spotPrice']),
            K=float(data['strikePrice']),
            T=float(data['timeToMaturity']),
            r=float(data['riskFreeRate']),
            option_type=data.get('optionType', 'call')
        )

        if iv is None:
            return jsonify({'error': 'Implied volatility calculation did not converge'}), 400

        return jsonify({'impliedVolatility': iv})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
