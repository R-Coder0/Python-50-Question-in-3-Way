def VowelCounter(string):
    vowels = set('aeiouAEIOU')
    return sum(1 for char in string if char in vowels)

string = input("Enter a string: ")
print("Vowel Count: ", VowelCounter(string))