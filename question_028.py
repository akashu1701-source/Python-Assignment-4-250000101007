# Simple interest using arguments and a return statement
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

p = float(input("Enter principal: "))
r = float(input("Enter annual interest rate (%): "))
t = float(input("Enter time in years: "))
print("Simple interest:", simple_interest(p, r, t))
