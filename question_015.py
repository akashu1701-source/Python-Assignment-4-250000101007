# Function to check whether a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")

check_even_odd(int(input("Enter an integer: ")))
