class SumOfDigit:
    def __init__(self, number):
        self.number = number
    def calculate_sum(self):
        
        n = abs(self.number)
        total = 0
        
        while n > 0:
            total += n % 10
            n //= 10
            
        return total
    
try:
    num = int(input("Enter a integer : "))
    
    digit_sum = SumOfDigit(num)
    
    result = digit_sum.calculate_sum()
    print("Sum of digits : ", result)
    
except ValueError:
    print("Invalid input! Please enter a integer.")