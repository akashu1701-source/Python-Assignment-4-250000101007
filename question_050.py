# Create a simple package with two modules and import from both.
# This script creates the package folder and its module files first.
from pathlib import Path
import importlib

package_dir = Path("student_package")
package_dir.mkdir(exist_ok=True)
(package_dir / "__init__.py").write_text("", encoding="utf-8")

(package_dir / "calculations.py").write_text(
    "def total(values):\n    return sum(values)\n", encoding="utf-8"
)
(package_dir / "messages.py").write_text(
    "def welcome(name):\n    return f'Welcome, {name}!'\n", encoding="utf-8"
)

calculations = importlib.import_module("student_package.calculations")
messages = importlib.import_module("student_package.messages")

print("Total:", calculations.total([10, 20, 30]))
print(messages.welcome("Student"))
