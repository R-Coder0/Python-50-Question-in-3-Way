class AnaGrams:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        
    def are_anagrams(self):
        str1 = self.str1.replace(" ", " ").lower()
        str2 = self.str2.replace(" ", " ").lower()
        
        if len(str1) != len(str2):
            return False
        return sorted(str1) ==  sorted(str2)
    
str1 = input("Enter the first String: ")
str2 = input("Enter the second string: ")

checker = AnaGrams(str1, str2)

if checker.are_anagrams():
    print("The string are anagrams.")
    
else:
    print("The string are not anagrams.")