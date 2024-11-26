def fibonacci_sequence(n):
    a, b = 0, 1
    sequence = []
    
    for _ in range(n):
        sequence.append(a)
        
        a, b = b, a + b
    return sequence

n = int(input("Enter the number of terms: "))

print("Fibonacci Sequence: ", " ".join(map(str, fibonacci_sequence(n))))