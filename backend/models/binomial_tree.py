"""Binomial Tree Option Pricing Model"""
import numpy as np


class BinomialTreeModel:
    """
    Implementation of the Binomial Tree option pricing model.

    The Binomial model discretizes the time to expiration into steps and models
    the underlying asset price as a binomial tree.
    """

    def __init__(self, S, K, T, r, sigma, steps=100, option_type='call', exercise='european'):
        """
        Initialize the Binomial Tree model.

        Args:
            S (float): Current stock price
            K (float): Strike price
            T (float): Time to maturity (in years)
            r (float): Risk-free interest rate (annual)
            sigma (float): Volatility of the underlying asset (annual)
            steps (int): Number of time steps in the tree
            option_type (str): 'call' or 'put'
            exercise (str): 'european' or 'american'
        """
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.steps = steps
        self.option_type = option_type.lower()
        self.exercise = exercise.lower()

        # Calculate tree parameters
        self.dt = T / steps
        self.u = np.exp(sigma * np.sqrt(self.dt))  # Up factor
        self.d = 1 / self.u  # Down factor
        self.p = (np.exp(r * self.dt) - self.d) / (self.u - self.d)  # Risk-neutral probability
        self.discount = np.exp(-r * self.dt)  # Discount factor

    def _build_stock_tree(self):
        """Build the stock price tree."""
        stock_tree = np.zeros((self.steps + 1, self.steps + 1))

        for i in range(self.steps + 1):
            for j in range(i + 1):
                stock_tree[j, i] = self.S * (self.u ** (i - j)) * (self.d ** j)

        return stock_tree

    def _calculate_option_value(self, stock_price):
        """Calculate option value at a given stock price."""
        if self.option_type == 'call':
            return max(0, stock_price - self.K)
        elif self.option_type == 'put':
            return max(0, self.K - stock_price)
        else:
            raise ValueError("option_type must be 'call' or 'put'")

    def price(self):
        """
        Calculate the option price using the Binomial Tree method.

        Returns:
            float: Option price
        """
        stock_tree = self._build_stock_tree()
        option_tree = np.zeros_like(stock_tree)

        # Calculate option values at maturity (final column)
        for j in range(self.steps + 1):
            option_tree[j, self.steps] = self._calculate_option_value(stock_tree[j, self.steps])

        # Backward induction through the tree
        for i in range(self.steps - 1, -1, -1):
            for j in range(i + 1):
                # Calculate option value from next period
                option_tree[j, i] = self.discount * (
                    self.p * option_tree[j, i + 1] + (1 - self.p) * option_tree[j + 1, i + 1]
                )

                # For American options, check early exercise
                if self.exercise == 'american':
                    exercise_value = self._calculate_option_value(stock_tree[j, i])
                    option_tree[j, i] = max(option_tree[j, i], exercise_value)

        return option_tree[0, 0]

    def get_tree(self):
        """
        Get the complete stock price tree and option value tree.

        Returns:
            tuple: (stock_tree, option_tree)
        """
        stock_tree = self._build_stock_tree()
        option_tree = np.zeros_like(stock_tree)

        # Calculate option values at maturity
        for j in range(self.steps + 1):
            option_tree[j, self.steps] = self._calculate_option_value(stock_tree[j, self.steps])

        # Backward induction
        for i in range(self.steps - 1, -1, -1):
            for j in range(i + 1):
                option_tree[j, i] = self.discount * (
                    self.p * option_tree[j, i + 1] + (1 - self.p) * option_tree[j + 1, i + 1]
                )

                if self.exercise == 'american':
                    exercise_value = self._calculate_option_value(stock_tree[j, i])
                    option_tree[j, i] = max(option_tree[j, i], exercise_value)

        return stock_tree, option_tree

    def delta(self):
        """
        Calculate Delta using the binomial tree.

        Returns:
            float: Delta value
        """
        stock_tree, option_tree = self.get_tree()

        # Delta at the root using the first two nodes
        delta = (option_tree[0, 1] - option_tree[1, 1]) / (stock_tree[0, 1] - stock_tree[1, 1])
        return delta

    def gamma(self):
        """
        Calculate Gamma using the binomial tree.

        Returns:
            float: Gamma value
        """
        stock_tree, option_tree = self.get_tree()

        # Gamma calculation using second derivatives
        delta_up = (option_tree[0, 2] - option_tree[1, 2]) / (stock_tree[0, 2] - stock_tree[1, 2])
        delta_down = (option_tree[1, 2] - option_tree[2, 2]) / (stock_tree[1, 2] - stock_tree[2, 2])
        gamma = (delta_up - delta_down) / ((stock_tree[0, 2] - stock_tree[2, 2]) / 2)

        return gamma
