import numpy as np
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma):
    """
    Calculate the Black-Scholes call and put option prices.

    Parameters:
    - S: float, current stock price
    - K: float, strike price
    - T: float, time to expiry in years
    - r: float, risk-free interest rate
    - sigma: float, volatility (standard deviation of the stock's returns)

    Returns:
    - tuple, (call option price, put option price)
    """
    # Calculate d1 and d2 using the Black-Scholes formula
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    # Calculate the call and put option prices
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    
    return call_price, put_price

# Example usage
if __name__ == "__main__":
    S = float(input("Enter current stock price: "))
    K = float(input("Enter strike price: "))
    T = float(input("Enter time to expiry in years: "))
    r = float(input("Enter risk-free interest rate (as a decimal): "))
    sigma = float(input("Enter volatility (as a decimal): "))

    call_price, put_price = black_scholes(S, K, T, r, sigma)
    print(f"The call option price is: {call_price:.2f}")
    print(f"The put option price is: {put_price:.2f}")
