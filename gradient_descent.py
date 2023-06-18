"""
Algorithm:
    1-Pick a random value from math function values
    2-Process and get it derivate
    3-Process descent random_fx_value - grad_value * learning_rate
    4-Update the random value = descent value from step 3
"""

import random

def fx(x):
    """
    Computes the value of the math function.

    Args:
        x (float): The input value.

    Returns:
        float: The result of the math function.
    """
    return 3 * x ** 2 - 3 * x + 4

def deriv(x):
    """
    Computes the derivative of the math function.

    Args:
        x (float): The input value.

    Returns:
        float: The derivative value.
    """
    return 6 * x - 3

# Set learning rate parameter
learning_rate = 0.01

# Number of training epochs
training_epochs = 100

# Generate a list of function values
fx_list = [fx(i) for i in range(100)]

# Choose a random value from the function values
random_x = random.choice(fx_list)
random_x_index = fx_list.index(random_x)

print(f"Random x value taken = {random_x}, index = {random_x_index}\n")

# Gradient descent algorithm
for epoch in range(training_epochs):
    # Compute the gradient
    grad = deriv(random_x)

    # Update the value of random_x using the gradient descent update rule
    random_x -= grad * learning_rate

    # Print the updated value and gradient
    print(f"Epoch {epoch+1}: random_x = {random_x}, gradient = {grad}\n")

print("local min =", random_x)