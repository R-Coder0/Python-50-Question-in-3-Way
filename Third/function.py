def is_palindrome(string):
    
    string = string.replace(" ", "").lower()
    
    return string == string[::-1]

user_input = input("Enter a string a check if it is a palindrome: ")

if is_palindrome(user_input):
    print(f"{user_input} is a palindrome. ")
    
else:
    print(f'{user_input} is not a palindrome. ')