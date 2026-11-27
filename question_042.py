# Create a module with arithmetic functions and use it.
from pathlib import Path
import importlib.util

module_code = """def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
"""
Path("arithmetic_module.py").write_text(module_code, encoding="utf-8")

spec = importlib.util.spec_from_file_location("arithmetic_module", "arithmetic_module.py")
arithmetic = importlib.util.module_from_spec(spec)
spec.loader.exec_module(arithmetic)

a, b = 12, 4
print("Addition:", arithmetic.add(a, b))
print("Subtraction:", arithmetic.subtract(a, b))
print("Multiplication:", arithmetic.multiply(a, b))
print("Division:", arithmetic.divide(a, b))
