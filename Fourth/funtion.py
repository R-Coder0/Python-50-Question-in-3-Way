def factorial_finder(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(1, n+ 1):
            fact *= i
        return fact
    
try:
    number = int(input("Enter a number to calculate its factorial : "))
    print(f'The factorial of {number} is: {factorial_finder(number)}.')

except ValueError:
    print("Please enter a valid integer.")
    