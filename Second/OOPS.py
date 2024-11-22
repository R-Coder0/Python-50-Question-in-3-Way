class StringManipulator:
    def __init__(self, string):
        self.string = string
        
    def reverse_string(self):
        reversed_string = ""
        for char in self.string:
            reversed_string = char + reversed_string
        return reversed_string
        
user_input = input("Enter a string to reverse : ")

string_mainpulator = StringManipulator(user_input)

print("Reversed String: ", string_mainpulator.reverse_string())