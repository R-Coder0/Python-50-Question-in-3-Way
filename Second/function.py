def reverse_string(string):
    reversed_string = ''
    
    for char in string:
        reversed_string = char + reversed_string
        
    return reversed_string

user_input = input("Enter the strign you want to reverse: ")

print("Reversed String: ", reverse_string(user_input))
