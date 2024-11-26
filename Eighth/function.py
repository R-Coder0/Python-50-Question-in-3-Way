def Sum_of_digit(n):
    total = 0
    
    n =abs(n)
    
    while n > 0:
        total += n % 10
        n //= 10
        
    return total

number = (int(input("Enter a intger : ")))

print(Sum_of_digit(number))