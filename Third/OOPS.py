class PalindromeChecker:
    def __init__(self, string):
        self.string = string
        
    def is_palindrome(self):
        
        normalized_string = self.string.replace(" ", "").lower()
        
        return normalized_string == normalized_string[::-1]
    
user_input = input("Enter a string to check if it is a palindrome: ")

checker = PalindromeChecker(user_input)

if checker.is_palindrome():
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")