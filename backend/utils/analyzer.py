"""Options Analysis Utilities"""
import numpy as np


class OptionsAnalyzer:
    """Utility class for analyzing options pricing results."""

    @staticmethod
    def compare_models(S, K, T, r, sigma, option_type='call'):
        """
        Compare prices from different pricing models.

        Args:
            S (float): Current stock price
            K (float): Strike price
            T (float): Time to maturity
            r (float): Risk-free rate
            sigma (float): Volatility
            option_type (str): 'call' or 'put'

        Returns:
            dict: Comparison results from all models
        """
        from ..models import BlackScholesModel, BinomialTreeModel, MonteCarloModel

        results = {}

        # Black-Scholes
        bs_model = BlackScholesModel(S, K, T, r, sigma, option_type)
        results['black_scholes'] = {
            'price': bs_model.price(),
            'greeks': bs_model.greeks()
        }

        # Binomial Tree
        bt_model = BinomialTreeModel(S, K, T, r, sigma, steps=100, option_type=option_type)
        results['binomial_tree'] = {
            'price': bt_model.price(),
            'delta': bt_model.delta(),
            'gamma': bt_model.gamma()
        }

        # Monte Carlo
        mc_model = MonteCarloModel(S, K, T, r, sigma, simulations=10000, option_type=option_type, seed=42)
        mc_result = mc_model.price_with_confidence()
        results['monte_carlo'] = {
            'price': mc_result['price'],
            'confidence_interval': [mc_result['lower_bound'], mc_result['upper_bound']],
            'std_error': mc_result['std_error']
        }

        return results

    @staticmethod
    def calculate_implied_volatility(market_price, S, K, T, r, option_type='call', max_iterations=100, tolerance=1e-5):
        """
        Calculate implied volatility using Newton-Raphson method.

        Args:
            market_price (float): Observed market price of the option
            S (float): Current stock price
            K (float): Strike price
            T (float): Time to maturity
            r (float): Risk-free rate
            option_type (str): 'call' or 'put'
            max_iterations (int): Maximum number of iterations
            tolerance (float): Convergence tolerance

        Returns:
            float: Implied volatility (or None if not converged)
        """
        from ..models import BlackScholesModel

        # Initial guess for volatility
        sigma = 0.3

        for i in range(max_iterations):
            model = BlackScholesModel(S, K, T, r, sigma, option_type)
            price = model.price()
            vega = model.vega() * 100  # Convert back to full vega

            price_diff = market_price - price

            if abs(price_diff) < tolerance:
                return sigma

            if vega == 0:
                return None

            # Newton-Raphson update
            sigma = sigma + price_diff / vega

            # Ensure sigma stays positive
            if sigma <= 0:
                sigma = 0.01

        return None  # Did not converge

    @staticmethod
    def payoff_diagram(S_range, K, premium, option_type='call', position='long'):
        """
        Calculate payoff and profit/loss for an options position.

        Args:
            S_range (numpy.ndarray): Range of spot prices
            K (float): Strike price
            premium (float): Option premium paid/received
            option_type (str): 'call' or 'put'
            position (str): 'long' or 'short'

        Returns:
            dict: Contains 'spot_prices', 'payoff', 'profit_loss'
        """
        if option_type == 'call':
            payoff = np.maximum(S_range - K, 0)
        else:
            payoff = np.maximum(K - S_range, 0)

        if position == 'long':
            profit_loss = payoff - premium
        else:  # short
            payoff = -payoff
            profit_loss = -payoff + premium

        return {
            'spot_prices': S_range.tolist(),
            'payoff': payoff.tolist(),
            'profit_loss': profit_loss.tolist()
        }

    @staticmethod
    def sensitivity_analysis(S, K, T, r, sigma, option_type='call', parameter='spot', variation_range=0.2):
        """
        Perform sensitivity analysis on a parameter.

        Args:
            S (float): Current stock price
            K (float): Strike price
            T (float): Time to maturity
            r (float): Risk-free rate
            sigma (float): Volatility
            option_type (str): 'call' or 'put'
            parameter (str): Parameter to vary ('spot', 'volatility', 'time', 'rate')
            variation_range (float): Percentage range to vary the parameter

        Returns:
            dict: Parameter values and corresponding option prices
        """
        from ..models import BlackScholesModel

        base_values = {'S': S, 'K': K, 'T': T, 'r': r, 'sigma': sigma}
        param_map = {'spot': 'S', 'volatility': 'sigma', 'time': 'T', 'rate': 'r'}

        if parameter not in param_map:
            raise ValueError(f"Invalid parameter: {parameter}")

        param_key = param_map[parameter]
        base_value = base_values[param_key]

        # Create range of values
        if parameter == 'time':
            param_values = np.linspace(max(0.01, base_value * (1 - variation_range)),
                                      base_value * (1 + variation_range), 50)
        else:
            param_values = np.linspace(base_value * (1 - variation_range),
                                      base_value * (1 + variation_range), 50)

        prices = []
        for value in param_values:
            params = base_values.copy()
            params[param_key] = value
            model = BlackScholesModel(params['S'], params['K'], params['T'],
                                     params['r'], params['sigma'], option_type)
            prices.append(model.price())

        return {
            'parameter': parameter,
            'values': param_values.tolist(),
            'prices': prices
        }
