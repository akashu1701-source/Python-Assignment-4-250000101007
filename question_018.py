# Function to check whether a number is prime
def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

n = int(input("Enter an integer: "))
print("Prime" if is_prime(n) else "Not prime")
