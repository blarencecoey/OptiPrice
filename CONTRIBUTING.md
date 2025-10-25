# Contributing to OptiPrice

Thank you for your interest in contributing to OptiPrice! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Submitting Changes](#submitting-changes)
- [Coding Standards](#coding-standards)
- [Testing](#testing)

## Code of Conduct

This project follows a standard Code of Conduct. Please be respectful and professional when interacting with other contributors.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/OptiPrice.git
   cd OptiPrice
   ```
3. **Add upstream remote**:
   ```bash
   git remote add upstream https://github.com/blarencecoey/OptiPrice.git
   ```
4. **Set up your development environment** (see [Development Setup](#development-setup))

## Development Setup

### Backend Development

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r backend/requirements.txt

# Install development dependencies (optional)
pip install pytest black flake8 mypy
```

### Frontend Development

```bash
# Install dependencies
npm install

# Install ESLint and Prettier (optional)
npm install --save-dev eslint prettier
```

## Making Changes

1. **Create a new branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

   Use descriptive branch names:
   - `feature/` for new features
   - `fix/` for bug fixes
   - `docs/` for documentation changes
   - `refactor/` for code refactoring

2. **Make your changes** following the [Coding Standards](#coding-standards)

3. **Test your changes** thoroughly

4. **Commit your changes** with clear, descriptive messages:
   ```bash
   git add .
   git commit -m "Add feature: description of what you added"
   ```

## Submitting Changes

1. **Update your fork** with the latest changes from upstream:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Push your changes** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create a Pull Request** on GitHub:
   - Go to your fork on GitHub
   - Click "Pull Request"
   - Provide a clear title and description
   - Reference any related issues

### Pull Request Guidelines

- Ensure your code follows the project's coding standards
- Include tests for new features
- Update documentation as needed
- Keep PRs focused on a single feature/fix
- Respond to feedback promptly

## Coding Standards

### Python (Backend)

- Follow [PEP 8](https://pep8.org/) style guide
- Use type hints where appropriate
- Write docstrings for all functions and classes:
  ```python
  def calculate_option_price(S, K, T, r, sigma):
      """
      Calculate option price using Black-Scholes model.

      Args:
          S (float): Current stock price
          K (float): Strike price
          T (float): Time to maturity
          r (float): Risk-free rate
          sigma (float): Volatility

      Returns:
          float: Option price
      """
      # Implementation
  ```
- Use meaningful variable names
- Keep functions focused and concise

### TypeScript/React (Frontend)

- Follow TypeScript best practices
- Use functional components with hooks
- Properly type all props and state:
  ```typescript
  interface CalculatorProps {
    spotPrice: number;
    strikePrice: number;
  }

  const Calculator: React.FC<CalculatorProps> = ({ spotPrice, strikePrice }) => {
    // Implementation
  };
  ```
- Use meaningful component and variable names
- Keep components focused and reusable

### General Guidelines

- Write clear, self-documenting code
- Add comments for complex logic
- Keep files focused on a single responsibility
- Avoid magic numbers (use named constants)
- Handle errors gracefully

## Testing

### Backend Tests

```bash
# Run tests
cd backend
python -m pytest

# Run with coverage
python -m pytest --cov=models --cov=utils
```

### Frontend Tests

```bash
# Run tests
npm test

# Run tests in watch mode
npm test -- --watch
```

### Manual Testing

Before submitting a PR, manually test:
1. All pricing models (Black-Scholes, Binomial Tree, Monte Carlo)
2. Model comparison functionality
3. Visualizations generate correctly
4. Error handling for invalid inputs
5. Both call and put options

## Areas for Contribution

We welcome contributions in the following areas:

### High Priority
- [ ] Unit tests for pricing models
- [ ] Integration tests for API endpoints
- [ ] Frontend component tests
- [ ] Input validation improvements
- [ ] Error handling enhancements

### Features
- [ ] Support for exotic options (Asian, Barrier, Lookback)
- [ ] Real-time market data integration
- [ ] Portfolio optimization tools
- [ ] Option strategy analyzer (spreads, straddles, etc.)
- [ ] Historical volatility calculations
- [ ] Risk metrics (VaR, CVaR)

### Improvements
- [ ] Performance optimization for Monte Carlo simulations
- [ ] Mobile responsiveness improvements
- [ ] Accessibility (WCAG compliance)
- [ ] Internationalization (i18n)
- [ ] Dark mode theme
- [ ] Export results to PDF/CSV

### Documentation
- [ ] API documentation with OpenAPI/Swagger
- [ ] Video tutorials
- [ ] Code examples and use cases
- [ ] Architecture documentation

## Questions?

If you have questions about contributing:
- Open an issue on GitHub
- Check existing issues for similar questions
- Review the [README.md](README.md) and [QUICKSTART.md](QUICKSTART.md)

## License

By contributing to OptiPrice, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to OptiPrice! Your efforts help make this project better for everyone.
