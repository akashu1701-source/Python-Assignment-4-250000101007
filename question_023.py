# Function to calculate the average of a list
def average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

values = [10, 20, 30, 40]
result = average(values)
print("Average:", result if result is not None else "List is empty")
