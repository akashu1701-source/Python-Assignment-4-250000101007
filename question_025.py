# Find string length without using len()
def string_length(text):
    count = 0
    for character in text:
        count += 1
    return count

text = input("Enter a string: ")
print("Length:", string_length(text))
