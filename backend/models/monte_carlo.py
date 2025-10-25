"""Monte Carlo Option Pricing Model"""
import numpy as np


class MonteCarloModel:
    """
    Implementation of the Monte Carlo option pricing model.

    Uses Monte Carlo simulation to price options by simulating many possible
    future price paths for the underlying asset.
    """

    def __init__(self, S, K, T, r, sigma, simulations=10000, option_type='call', seed=None):
        """
        Initialize the Monte Carlo model.

        Args:
            S (float): Current stock price
            K (float): Strike price
            T (float): Time to maturity (in years)
            r (float): Risk-free interest rate (annual)
            sigma (float): Volatility of the underlying asset (annual)
            simulations (int): Number of simulation paths
            option_type (str): 'call' or 'put'
            seed (int): Random seed for reproducibility
        """
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.simulations = simulations
        self.option_type = option_type.lower()
        self.seed = seed

        if seed is not None:
            np.random.seed(seed)

    def _simulate_paths(self, steps=100):
        """
        Simulate price paths using Geometric Brownian Motion.

        Args:
            steps (int): Number of time steps in each path

        Returns:
            numpy.ndarray: Array of simulated price paths
        """
        dt = self.T / steps
        paths = np.zeros((self.simulations, steps + 1))
        paths[:, 0] = self.S

        for t in range(1, steps + 1):
            z = np.random.standard_normal(self.simulations)
            paths[:, t] = paths[:, t - 1] * np.exp(
                (self.r - 0.5 * self.sigma**2) * dt + self.sigma * np.sqrt(dt) * z
            )

        return paths

    def price(self, steps=100):
        """
        Calculate the option price using Monte Carlo simulation.

        Args:
            steps (int): Number of time steps in each simulation path

        Returns:
            float: Option price
        """
        paths = self._simulate_paths(steps)
        final_prices = paths[:, -1]

        if self.option_type == 'call':
            payoffs = np.maximum(final_prices - self.K, 0)
        elif self.option_type == 'put':
            payoffs = np.maximum(self.K - final_prices, 0)
        else:
            raise ValueError("option_type must be 'call' or 'put'")

        # Discount the expected payoff to present value
        option_price = np.exp(-self.r * self.T) * np.mean(payoffs)
        return option_price

    def price_with_confidence(self, steps=100, confidence=0.95):
        """
        Calculate option price with confidence interval.

        Args:
            steps (int): Number of time steps in each simulation path
            confidence (float): Confidence level (e.g., 0.95 for 95%)

        Returns:
            dict: Dictionary with 'price', 'std', 'lower_bound', 'upper_bound'
        """
        paths = self._simulate_paths(steps)
        final_prices = paths[:, -1]

        if self.option_type == 'call':
            payoffs = np.maximum(final_prices - self.K, 0)
        else:
            payoffs = np.maximum(self.K - final_prices, 0)

        discounted_payoffs = np.exp(-self.r * self.T) * payoffs

        price = np.mean(discounted_payoffs)
        std = np.std(discounted_payoffs)
        std_error = std / np.sqrt(self.simulations)

        # Calculate confidence interval using normal approximation
        from scipy.stats import norm
        z_score = norm.ppf((1 + confidence) / 2)

        return {
            'price': price,
            'std': std,
            'std_error': std_error,
            'lower_bound': price - z_score * std_error,
            'upper_bound': price + z_score * std_error
        }

    def get_paths(self, num_paths=100, steps=100):
        """
        Get a subset of simulated paths for visualization.

        Args:
            num_paths (int): Number of paths to return
            steps (int): Number of time steps in each path

        Returns:
            numpy.ndarray: Array of simulated price paths
        """
        # Temporarily change simulations count
        original_simulations = self.simulations
        self.simulations = num_paths

        paths = self._simulate_paths(steps)

        # Restore original simulations count
        self.simulations = original_simulations

        return paths

    def delta(self, bump=0.01):
        """
        Calculate Delta using finite difference method.

        Args:
            bump (float): Size of the price bump for finite difference

        Returns:
            float: Delta value
        """
        # Price with current stock price
        price_original = self.price()

        # Price with bumped stock price
        original_S = self.S
        self.S = original_S * (1 + bump)
        price_bumped = self.price()

        # Restore original stock price
        self.S = original_S

        # Calculate delta using finite difference
        delta = (price_bumped - price_original) / (original_S * bump)
        return delta

    def vega(self, bump=0.01):
        """
        Calculate Vega using finite difference method.

        Args:
            bump (float): Size of the volatility bump

        Returns:
            float: Vega value
        """
        # Price with current volatility
        price_original = self.price()

        # Price with bumped volatility
        original_sigma = self.sigma
        self.sigma = original_sigma + bump
        price_bumped = self.price()

        # Restore original volatility
        self.sigma = original_sigma

        # Calculate vega
        vega = (price_bumped - price_original) / bump / 100
        return vega
