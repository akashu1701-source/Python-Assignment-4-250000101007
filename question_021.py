# Function to calculate the sum of digits of an integer
def sum_of_digits(number):
    total = 0
    for digit in str(abs(number)):
        total += int(digit)
    return total

n = int(input("Enter an integer: "))
print("Sum of digits:", sum_of_digits(n))
