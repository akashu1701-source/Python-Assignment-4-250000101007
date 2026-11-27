# Factorial using the math module
import math
number = int(input("Enter a non-negative integer: "))
if number >= 0:
    print("Factorial:", math.factorial(number))
else:
    print("Factorial is not defined for negative integers.")
