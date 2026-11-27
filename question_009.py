# Sine, cosine and tangent of an angle (entered in degrees)
import math
degrees = float(input("Enter angle in degrees: "))
radians = math.radians(degrees)
print("Sine:", math.sin(radians))
print("Cosine:", math.cos(radians))
if math.isclose(math.cos(radians), 0.0, abs_tol=1e-12):
    print("Tangent is undefined for this angle.")
else:
    print("Tangent:", math.tan(radians))
