# Local and global variables with the same name
number = 100  # Global variable

def show_number():
    number = 25  # Local variable
    print("Local number:", number)

show_number()
print("Global number:", number)
