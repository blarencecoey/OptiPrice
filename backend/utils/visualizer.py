"""Options Pricing Visualization Utilities"""
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import io
import base64


class OptionsVisualizer:
    """Utility class for creating visualizations of options pricing data."""

    @staticmethod
    def plot_option_price_vs_spot(model_class, K, T, r, sigma, spot_range, option_type='call', **kwargs):
        """
        Plot option price vs spot price.

        Args:
            model_class: The pricing model class to use
            K (float): Strike price
            T (float): Time to maturity
            r (float): Risk-free rate
            sigma (float): Volatility
            spot_range (tuple): (min_spot, max_spot)
            option_type (str): 'call' or 'put'
            **kwargs: Additional parameters for the model

        Returns:
            str: Base64 encoded PNG image
        """
        spot_prices = np.linspace(spot_range[0], spot_range[1], 100)
        option_prices = []

        for S in spot_prices:
            model = model_class(S, K, T, r, sigma, option_type=option_type, **kwargs)
            option_prices.append(model.price())

        plt.figure(figsize=(10, 6))
        plt.plot(spot_prices, option_prices, linewidth=2)
        plt.xlabel('Spot Price', fontsize=12)
        plt.ylabel('Option Price', fontsize=12)
        plt.title(f'{option_type.capitalize()} Option Price vs Spot Price', fontsize=14)
        plt.grid(True, alpha=0.3)
        plt.axvline(x=K, color='r', linestyle='--', label=f'Strike = {K}')
        plt.legend()

        return OptionsVisualizer._fig_to_base64()

    @staticmethod
    def plot_greeks(model_class, K, T, r, sigma, spot_range, option_type='call', **kwargs):
        """
        Plot Greeks (Delta, Gamma, Vega, Theta) vs spot price.

        Args:
            model_class: The pricing model class to use
            K (float): Strike price
            T (float): Time to maturity
            r (float): Risk-free rate
            sigma (float): Volatility
            spot_range (tuple): (min_spot, max_spot)
            option_type (str): 'call' or 'put'

        Returns:
            str: Base64 encoded PNG image
        """
        spot_prices = np.linspace(spot_range[0], spot_range[1], 100)
        deltas, gammas, vegas, thetas = [], [], [], []

        for S in spot_prices:
            model = model_class(S, K, T, r, sigma, option_type=option_type, **kwargs)
            deltas.append(model.delta())
            if hasattr(model, 'gamma'):
                gammas.append(model.gamma())
            if hasattr(model, 'vega'):
                vegas.append(model.vega())
            if hasattr(model, 'theta'):
                thetas.append(model.theta())

        fig, axes = plt.subplots(2, 2, figsize=(14, 10))

        # Delta
        axes[0, 0].plot(spot_prices, deltas, linewidth=2, color='blue')
        axes[0, 0].set_xlabel('Spot Price')
        axes[0, 0].set_ylabel('Delta')
        axes[0, 0].set_title('Delta vs Spot Price')
        axes[0, 0].grid(True, alpha=0.3)
        axes[0, 0].axvline(x=K, color='r', linestyle='--', alpha=0.5)

        # Gamma
        if gammas:
            axes[0, 1].plot(spot_prices, gammas, linewidth=2, color='green')
            axes[0, 1].set_xlabel('Spot Price')
            axes[0, 1].set_ylabel('Gamma')
            axes[0, 1].set_title('Gamma vs Spot Price')
            axes[0, 1].grid(True, alpha=0.3)
            axes[0, 1].axvline(x=K, color='r', linestyle='--', alpha=0.5)

        # Vega
        if vegas:
            axes[1, 0].plot(spot_prices, vegas, linewidth=2, color='orange')
            axes[1, 0].set_xlabel('Spot Price')
            axes[1, 0].set_ylabel('Vega')
            axes[1, 0].set_title('Vega vs Spot Price')
            axes[1, 0].grid(True, alpha=0.3)
            axes[1, 0].axvline(x=K, color='r', linestyle='--', alpha=0.5)

        # Theta
        if thetas:
            axes[1, 1].plot(spot_prices, thetas, linewidth=2, color='red')
            axes[1, 1].set_xlabel('Spot Price')
            axes[1, 1].set_ylabel('Theta')
            axes[1, 1].set_title('Theta vs Spot Price')
            axes[1, 1].grid(True, alpha=0.3)
            axes[1, 1].axvline(x=K, color='r', linestyle='--', alpha=0.5)

        plt.tight_layout()
        return OptionsVisualizer._fig_to_base64()

    @staticmethod
    def plot_monte_carlo_paths(paths, K, option_type='call'):
        """
        Plot Monte Carlo simulation paths.

        Args:
            paths (numpy.ndarray): Array of simulated price paths
            K (float): Strike price
            option_type (str): 'call' or 'put'

        Returns:
            str: Base64 encoded PNG image
        """
        plt.figure(figsize=(12, 7))

        # Plot paths
        time_steps = np.arange(paths.shape[1])
        for i in range(min(100, paths.shape[0])):  # Plot up to 100 paths
            plt.plot(time_steps, paths[i], alpha=0.3, linewidth=0.5)

        # Plot mean path
        mean_path = np.mean(paths, axis=0)
        plt.plot(time_steps, mean_path, 'b-', linewidth=2, label='Mean Path')

        plt.axhline(y=K, color='r', linestyle='--', linewidth=2, label=f'Strike = {K}')
        plt.xlabel('Time Steps', fontsize=12)
        plt.ylabel('Stock Price', fontsize=12)
        plt.title('Monte Carlo Simulated Price Paths', fontsize=14)
        plt.legend()
        plt.grid(True, alpha=0.3)

        return OptionsVisualizer._fig_to_base64()

    @staticmethod
    def plot_volatility_surface(model_class, spot_price, strikes, maturities, r, sigma, option_type='call'):
        """
        Plot implied volatility surface.

        Args:
            model_class: The pricing model class to use
            spot_price (float): Current spot price
            strikes (list): List of strike prices
            maturities (list): List of time to maturities
            r (float): Risk-free rate
            sigma (float): Base volatility
            option_type (str): 'call' or 'put'

        Returns:
            str: Base64 encoded PNG image
        """
        from mpl_toolkits.mplot3d import Axes3D

        K_grid, T_grid = np.meshgrid(strikes, maturities)
        prices = np.zeros_like(K_grid)

        for i in range(len(maturities)):
            for j in range(len(strikes)):
                model = model_class(spot_price, K_grid[i, j], T_grid[i, j], r, sigma, option_type=option_type)
                prices[i, j] = model.price()

        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        surf = ax.plot_surface(K_grid, T_grid, prices, cmap='viridis', alpha=0.8)

        ax.set_xlabel('Strike Price', fontsize=11)
        ax.set_ylabel('Time to Maturity', fontsize=11)
        ax.set_zlabel('Option Price', fontsize=11)
        ax.set_title(f'{option_type.capitalize()} Option Price Surface', fontsize=14)
        fig.colorbar(surf, shrink=0.5, aspect=5)

        return OptionsVisualizer._fig_to_base64()

    @staticmethod
    def _fig_to_base64():
        """Convert current matplotlib figure to base64 string."""
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=100, bbox_inches='tight')
        plt.close()
        buf.seek(0)
        img_base64 = base64.b64encode(buf.read()).decode('utf-8')
        return img_base64
