class FactorialCalculator:
    def __init__(self, number):
        self.number = number
        
    def calculate_factorial(self):
        if self.number < 0:
            return "Factorial is not defined for negative numbers."
        
        elif self.number == 0 or self.number == 1:
            return 1
        else:
            factorial = 1
            for i in range(1, self.number + 1):
                factorial *= i
            return factorial
        
try:
    number = int(input("Enter a number to calculate the factorial : "))
    
    factorial_calculator = FactorialCalculator(number)
    
    print(f'The factorial of {number} is : {factorial_calculator.calculate_factorial()}')
    
except ValueError:
    print("Please Enter a valid integer.")