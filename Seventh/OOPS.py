class VowelCounter:
    def __init__(self,string):
        self.string = string
        self.vowels = set('aeiouAEIOU')
        
    def count_vowels(self):
        return sum(1 for char in self.string if char in self.vowels)
    
string = input("Enter a string : ")
vowel_counter = VowelCounter(string)
print("Vowel Count : ", vowel_counter.count_vowels())