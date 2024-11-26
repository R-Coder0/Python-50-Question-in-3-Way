try:
    string = input("Enter a string: ")
    vowels = 'aeiouAEIOU'

    count = 0

    for char in string:
        if char in vowels:
            count += 1
    print("Vowel Count:", count)

except Exception as e:
    print("An error occurred. Please enter a valid string.")
    print("Error details:", e)
