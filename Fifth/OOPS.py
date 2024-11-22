class SecondLargestFinder:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def find(self):
        if len(self.numbers) < 2:
            return "List must have at least two elements to find the second largest number."
        
        largest = second_largest = float('-inf')
        
        for number in self.numbers:
            if number > largest:
                second_largest = largest
                largest = number
                
            elif number > second_largest and number != largest:
               second_largest = number
        if second_largest == float('-inf'):
             return "No second largest elements exists(all elements are the same)"
        else:
            return second_largest
        
try:
    input_list = list(map(int, input('Enter the list of number : ').split()))
    finder = SecondLargestFinder(input_list)
    result = finder.find()
    print(f'The second largest element is: {result}' if isinstance(result, int) else result)
    
except ValueError:
    print("Please enter a valid list of integers.")