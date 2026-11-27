# Function to find the largest element in a list
def largest(numbers):
    if not numbers:
        return None
    return max(numbers)

values = [8, 19, 4, 25, 11]
print("Largest element:", largest(values))
