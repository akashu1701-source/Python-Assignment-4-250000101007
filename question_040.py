# Two functions can use local variables with the same name
def first_function():
    value = 10
    print("Value in first_function:", value)

def second_function():
    value = 50
    print("Value in second_function:", value)

first_function()
second_function()
