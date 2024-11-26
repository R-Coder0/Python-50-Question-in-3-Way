number = int(input("Enter a integer : "))

total = 0

n = abs(number)

while n>0:
    total += n % 10
    n //= 10
    
print("Sum of digits : ", total)