# Square root using the math module
import math
number = float(input("Enter a non-negative number: "))
if number >= 0:
    print("Square root:", math.sqrt(number))
else:
    print("Please enter a non-negative number.")
