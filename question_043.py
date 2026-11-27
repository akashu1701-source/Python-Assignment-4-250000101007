# Import math and calculate square root and factorial
import math

number = int(input("Enter a non-negative integer: "))
if number >= 0:
    print("Square root:", math.sqrt(number))
    print("Factorial:", math.factorial(number))
else:
    print("Please enter a non-negative integer.")
