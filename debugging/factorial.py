#!/usr/bin/python3
import sys

def factorial(n):
    """Return the factorial of a given integer n."""
    result = 1
    while n > 1:
        result *= n
        n -= 1   # decrement to avoid infinite loop
    return result

if __name__ == "__main__":
    f = factorial(int(sys.argv[1]))
    print(f)
