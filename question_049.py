# Create a student-marks module and use its functions.
from pathlib import Path
import importlib.util

module_code = """def total_marks(marks):
    return sum(marks)

def average_marks(marks):
    return sum(marks) / len(marks) if marks else 0

def percentage(marks, maximum_per_subject=100):
    if not marks or maximum_per_subject <= 0:
        return 0
    return (sum(marks) / (len(marks) * maximum_per_subject)) * 100
"""
Path("student_marks.py").write_text(module_code, encoding="utf-8")

spec = importlib.util.spec_from_file_location("student_marks", "student_marks.py")
student_marks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student_marks)

marks = [78, 85, 92, 69, 88]
print("Marks:", marks)
print("Total:", student_marks.total_marks(marks))
print("Average:", student_marks.average_marks(marks))
print("Percentage:", student_marks.percentage(marks), "%")
