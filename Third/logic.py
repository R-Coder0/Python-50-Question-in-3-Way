
string = input("Enter a string to check if it is a palindrome: ")

normalized_string = string.replace(" ", "").lower()

reversed_string = ""
for char in normalized_string:
    reversed_string = char + reversed_string
    
    
if normalized_string == reversed_string:
    print(f"{string} is a palindrome. ")
else:
    print(f"{string} is not a palindrome.")