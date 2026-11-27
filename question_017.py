# Function to calculate factorial
def factorial(number):
    if number < 0:
        return None
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result

n = int(input("Enter a non-negative integer: "))
answer = factorial(n)
if answer is None:
    print("Factorial is not defined for negative integers.")
else:
    print("Factorial:", answer)
