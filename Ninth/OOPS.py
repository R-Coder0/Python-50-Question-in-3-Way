class FibonacciSequence:
    def __init__(self, n):
        self.n = n
        
    def generate_sequence(self):
        a, b = 0, 1
        sequence = []
        
        for _ in range(n):
            sequence.append(a)
            
            a, b = b, a + b
        return sequence

n = int(input("Enter the number of terms: "))

Fibonacci = FibonacciSequence(n)

print("Fibonacci Sequence: ", " ".join(map(str, Fibonacci.generate_sequence())))