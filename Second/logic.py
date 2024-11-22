# Reverse the string using for loop.
str = input("Enter the dtring you want to repeat: ")

str_reverse = ""

for char in str:
    str_reverse = char + str_reverse
    
print(f'{str_reverse} is the reversed string.')