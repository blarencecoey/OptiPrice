"""Black-Scholes Option Pricing Model"""
import numpy as np
from scipy.stats import norm


class BlackScholesModel:
    """
    Implementation of the Black-Scholes option pricing model.

    The Black-Scholes model is used to calculate the theoretical price of European options.
    """

    def __init__(self, S, K, T, r, sigma, option_type='call'):
        """
        Initialize the Black-Scholes model.

        Args:
            S (float): Current stock price
            K (float): Strike price
            T (float): Time to maturity (in years)
            r (float): Risk-free interest rate (annual)
            sigma (float): Volatility of the underlying asset (annual)
            option_type (str): 'call' or 'put'
        """
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.option_type = option_type.lower()

    def _calculate_d1_d2(self):
        """Calculate d1 and d2 parameters for Black-Scholes formula."""
        d1 = (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma**2) * self.T) / (self.sigma * np.sqrt(self.T))
        d2 = d1 - self.sigma * np.sqrt(self.T)
        return d1, d2

    def price(self):
        """
        Calculate the option price using Black-Scholes formula.

        Returns:
            float: Option price
        """
        d1, d2 = self._calculate_d1_d2()

        if self.option_type == 'call':
            price = self.S * norm.cdf(d1) - self.K * np.exp(-self.r * self.T) * norm.cdf(d2)
        elif self.option_type == 'put':
            price = self.K * np.exp(-self.r * self.T) * norm.cdf(-d2) - self.S * norm.cdf(-d1)
        else:
            raise ValueError("option_type must be 'call' or 'put'")

        return price

    def delta(self):
        """
        Calculate Delta (rate of change of option price with respect to underlying price).

        Returns:
            float: Delta value
        """
        d1, _ = self._calculate_d1_d2()

        if self.option_type == 'call':
            return norm.cdf(d1)
        else:
            return norm.cdf(d1) - 1

    def gamma(self):
        """
        Calculate Gamma (rate of change of delta with respect to underlying price).

        Returns:
            float: Gamma value
        """
        d1, _ = self._calculate_d1_d2()
        return norm.pdf(d1) / (self.S * self.sigma * np.sqrt(self.T))

    def vega(self):
        """
        Calculate Vega (sensitivity to volatility).

        Returns:
            float: Vega value (divided by 100 for percentage change)
        """
        d1, _ = self._calculate_d1_d2()
        return self.S * norm.pdf(d1) * np.sqrt(self.T) / 100

    def theta(self):
        """
        Calculate Theta (time decay of option).

        Returns:
            float: Theta value (per day)
        """
        d1, d2 = self._calculate_d1_d2()

        if self.option_type == 'call':
            theta = (-self.S * norm.pdf(d1) * self.sigma / (2 * np.sqrt(self.T))
                     - self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(d2))
        else:
            theta = (-self.S * norm.pdf(d1) * self.sigma / (2 * np.sqrt(self.T))
                     + self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(-d2))

        return theta / 365  # Convert to daily theta

    def rho(self):
        """
        Calculate Rho (sensitivity to interest rate).

        Returns:
            float: Rho value (divided by 100 for percentage change)
        """
        _, d2 = self._calculate_d1_d2()

        if self.option_type == 'call':
            return self.K * self.T * np.exp(-self.r * self.T) * norm.cdf(d2) / 100
        else:
            return -self.K * self.T * np.exp(-self.r * self.T) * norm.cdf(-d2) / 100

    def greeks(self):
        """
        Calculate all Greeks at once.

        Returns:
            dict: Dictionary containing all Greek values
        """
        return {
            'delta': self.delta(),
            'gamma': self.gamma(),
            'vega': self.vega(),
            'theta': self.theta(),
            'rho': self.rho()
        }
