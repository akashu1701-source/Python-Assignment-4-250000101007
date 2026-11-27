# Count uppercase and lowercase characters
def count_cases(text):
    uppercase = sum(1 for ch in text if ch.isupper())
    lowercase = sum(1 for ch in text if ch.islower())
    return uppercase, lowercase

text = input("Enter a string: ")
upper_count, lower_count = count_cases(text)
print("Uppercase characters:", upper_count)
print("Lowercase characters:", lower_count)
