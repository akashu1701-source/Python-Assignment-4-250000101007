# Import a specific function from a module
from math import sqrt

number = float(input("Enter a non-negative number: "))
if number >= 0:
    print("Square root:", sqrt(number))
else:
    print("Please enter a non-negative number.")
