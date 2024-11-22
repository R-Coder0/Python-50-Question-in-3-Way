def find_second_largest(numbers):
    if len(numbers) < 2:
        return "List must have at least two elements to find the second largest number."
    
    largest = second_largest = float('-inf')
    
    for number in numbers:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest and number != largest:
            second_largest = number
    if second_largest == float('-inf'):
        return "No second largest elements exists(all elements are the same)."
    else:
        return second_largest
    
try:
    input_list = list(map(int, input('Enter the list of number : ').split()))
    result = find_second_largest(input_list)
    print(f'The second largest element is : {result}' if isinstance(result, int) else result)
    
except:
    print('Please entere a valid list of integers.')
        
        