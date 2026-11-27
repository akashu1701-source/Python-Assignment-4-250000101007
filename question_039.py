# Modify a global variable using the global keyword
count = 10

def update_count():
    global count
    count = 25

print("Before:", count)
update_count()
print("After:", count)
