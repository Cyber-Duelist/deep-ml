import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    """
    Perform linear regression using gradient descent.
    
    Args:
        X: Feature matrix of shape (m, n) where first column is all ones (for intercept)
        y: Target vector of shape (m,)
        alpha: Learning rate
        iterations: Number of gradient descent iterations
        
    Returns:
        Learned weights as a 1D array of shape (n,)
    """
    m, n = X.shape
    y = y.reshape(-1, 1)  # Ensure y is a column vector of shape (m, 1)
    theta = np.zeros((n, 1))  # Initialize weights to zeros

    for _ in range(iterations):
        # Compute predictions: h_theta(X) = X @ theta
        predictions = X @ theta
        
        # Calculate error: (h_theta(X) - y)
        errors = predictions - y
        
        # Compute gradient: (1/m) * X^T @ (X @ theta - y)
        gradient = (1 / m) * (X.T @ errors)
        
        # Update parameters
        theta -= alpha * gradient

    # Flatten theta back to a 1D array of shape (n,)
    return theta.flatten()