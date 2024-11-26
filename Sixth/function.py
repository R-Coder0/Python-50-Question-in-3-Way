def are_anagrams(str1, str2):
    str1 = str1.replace(" "," ").lower()
    str2 = str2.replace(" "," ").lower()
    
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)

str1 = input("Enter the first String: ")
str2 = input("Enter the second string: ")

if are_anagrams(str1, str2):
    print("The strings are anagrams.")
    
else:
    print("The string are not anagrams")