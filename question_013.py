# Function to calculate the area of a circle
import math

def circle_area(radius):
    return math.pi * radius * radius

r = float(input("Enter circle radius: "))
if r >= 0:
    print("Area:", circle_area(r))
else:
    print("Radius cannot be negative.")
