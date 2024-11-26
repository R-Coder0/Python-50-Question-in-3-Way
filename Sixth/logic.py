
str1 = input("Enter the first string: ").replace(" ", "").lower()
str2 = input("Enter the second string: ").replace(" ", "").lower()


if len(str1) != len(str2):
    print("The strings are not anagrams.")
else:

    if sorted(str1) == sorted(str2):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")