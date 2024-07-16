import numpy as np
from scipy.stats import norm

def black_scholes(option_type, S, K, T, r, sigma):
    """
    Calculate the Black-Scholes option price.

    Parameters:
    - option_type: str, 'call' or 'put'
    - S: float, current stock price
    - K: float, strike price
    - T: float, time to expiry in years
    - r: float, risk-free interest rate
    - sigma: float, volatility (standard deviation of the stock's returns)

    Returns:
    - float, the calculated option price
    """
    # Calculate d1 and d2 using the Black-Scholes formula
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    # Calculate the option price based on the type
    if option_type == 'call':
        option_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        option_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Option type must be 'call' or 'put'")
    
    return option_price

# Example usage
if __name__ == "__main__":
    option_type = input("Enter option type ('call' or 'put'): ").strip().lower()
    S = float(input("Enter current stock price: "))
    K = float(input("Enter strike price: "))
    T = float(input("Enter time to expiry in years: "))
    r = float(input("Enter risk-free interest rate (as a decimal): "))
    sigma = float(input("Enter volatility (as a decimal): "))

    option_price = black_scholes(option_type, S, K, T, r, sigma)
    print(f"The {option_type} option price is: {option_price:.2f}")
