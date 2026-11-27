# Function to count vowels in a string
def count_vowels(text):
    return sum(1 for character in text.lower() if character in "aeiou")

text = input("Enter a string: ")
print("Number of vowels:", count_vowels(text))
