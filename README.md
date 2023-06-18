# Gradient-Descent-Algorithm-in-1-Dimension
This repository contains an implementation of the gradient descent algorithm in one dimension. Gradient descent is a popular optimization algorithm used to find the minimum of a function. It iteratively adjusts the parameters of the function in the direction of steepest descent, guided by the gradient of the function.

## Introduction

The Gradient Descent algorithm is widely used in various fields, including machine learning, optimization, and data analysis. This repository provides a simple and efficient implementation of the Gradient Descent algorithm specifically designed for one-dimensional functions.

Key features of this implementation include:

- **Gradient Calculation**: The repository provides a function to calculate the gradient of a given function in one dimension. The gradient indicates the direction of steepest descent, allowing the algorithm to iteratively update the parameters.

- **Learning Rate Optimization**: The algorithm supports various strategies for determining an optimal learning rate. These strategies, such as fixed learning rate, adaptive learning rate, or line search, ensure effective convergence and avoid overshooting or slow convergence issues.

- **Convergence Criteria**: This implementation includes customizable convergence criteria to terminate the optimization process. Users can define stopping conditions such as a maximum number of iterations, a threshold for the change in function value, or a desired level of accuracy.

- **Visualization**: The repository provides visualization tools to aid in understanding the optimization process. It includes interactive plots that display the function, the current position, and the trajectory of the algorithm throughout the iterations.

## Usage

To use this implementation of the Gradient Descent algorithm, follow these steps:

1. Clone the repository to your local machine using the following command:

   ```shell
   git clone https://github.com/your-username/gradient-descent-1d.git
   ```
   
## Examples

To demonstrate the usage of the Gradient Descent algorithm in one dimension, the repository includes an example script, example.py. This script showcases how to use the algorithm to optimize a simple one-dimensional function.

You can run the example script by executing the following command:

   ```shell 
   python gradient_descent.py
   ```
   
## License

This repository is licensed under the [MIT License](LICENSE).

You are free to use, modify, and distribute the code for personal or commercial purposes.

