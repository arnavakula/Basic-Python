"""
factorial(n) = n * factorial(n-1)
first, set up a condition to stop
replace functions with return values to better understand
"""

def factorial(n):
    if(n == 0):
        result = 1
    else:
        result = n * factorial(n - 1)
    return result

print(factorial(5))
 