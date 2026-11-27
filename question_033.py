# Function accepts a list and returns its largest element
def largest_element(values):
    if not values:
        return None
    return max(values)

numbers = [7, 31, 12, 4, 18]
print("Largest element:", largest_element(numbers))
