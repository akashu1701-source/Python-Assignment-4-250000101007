# Demonstrate local variables inside a function
def show_local():
    message = "I am a local variable"
    print(message)

show_local()
# message cannot be accessed here because it is local to show_local().
