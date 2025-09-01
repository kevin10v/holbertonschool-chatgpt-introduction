#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
        Calculate the factorial of a number using recursion.

    Parameters:
        n (int): A non-negative integer for which the factorial is calculated.

    Returns:
        int: The factorial of the given number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Read integer from command line argument and compute factorial
f = factorial(int(sys.argv[1]))
print(f)
