# Function to check whether a string is a palindrome
def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

word = input("Enter a word or phrase: ")
print("Palindrome" if is_palindrome(word) else "Not a palindrome")
