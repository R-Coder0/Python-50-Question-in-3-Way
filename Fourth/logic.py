try:
    number = int(input("Enter a number to calculate the factorial : "))
    
    if number < 0:
        print("Factorical is not defined for negative numbers.")
        
    elif number == 0 or number == 1:
        print(f"The factorial of {number} is : 1")
        
    else:
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i
        print (f"The factorial of {number} is {factorial}")
        
except ValueError:
    print(f'Please enter a valid integer.')