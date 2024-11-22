# Input from the user
str1 = input("Enter the first string: ").replace(" ", "").lower()
str2 = input("Enter the second string: ").replace(" ", "").lower()

# Check if lengths are the same
if len(str1) != len(str2):
    print("The strings are not anagrams.")
else:
    # Sort and compare
    if sorted(str1) == sorted(str2):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")