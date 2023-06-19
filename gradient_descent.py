"""
Algorithm:
    1-Pick a random value from cost function values
    2-Process and get it derivate
    3-Process descent random_fx_value -= grad_value * learning_rate
"""

import random

def fx(x: float) -> float:
    """
    Computes the value of the math function.

    Args:
        x (float): The input value.

    Returns:
        float: The result of the math function.
    """
    return x ** 2 

def deriv(x: float) -> float:
    """
    Computes the derivative of the math function.

    Args:
        x (float): The input value.

    Returns:
        float: The derivative value.
    """
    return 2 * x
    
# Set learning rate parameter
learning_rate = 0.01

# Threshold to finish trainig once the difference between currnet iteration and last one is equals or lower than
threshold = 0.0001

# Number of training epochs
training_epochs = 100

# Generate a list of values from 0 to 100 with the fx(x) function
fx_list = [fx(i) for i in range(100)]

# Choose a random value from the function values
random_x = random.choice(fx_list)

print(f"Random x value taken = {random_x}\n")

# Gradient descent algorithm
for epoch in range(training_epochs):
    # Compute the derivate
    grad = deriv(random_x)

    # Update the value of random_x using the gradient descent update rule
    random_x -= grad * learning_rate

print("local min in cost function =", random_x)