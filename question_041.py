# Create a user-defined module, then import its square() function.
# Run this file in a folder where it is allowed to create files.
from pathlib import Path
import importlib.util

module_code = "def square(number):\n    return number * number\n"
Path("square_module.py").write_text(module_code, encoding="utf-8")

spec = importlib.util.spec_from_file_location("square_module", "square_module.py")
square_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(square_module)

n = int(input("Enter a number: "))
print("Square:", square_module.square(n))
