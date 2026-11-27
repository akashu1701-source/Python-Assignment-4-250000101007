# Demonstrate ceil(), floor() and sqrt()
import math
number = float(input("Enter a non-negative number: "))
if number >= 0:
    print("Ceiling:", math.ceil(number))
    print("Floor:", math.floor(number))
    print("Square root:", math.sqrt(number))
else:
    print("Please enter a non-negative number.")
