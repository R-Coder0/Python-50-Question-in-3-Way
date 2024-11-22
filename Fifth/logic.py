try:
    input_list = list(map(int, input("Enter the list of number : ").split()))
    
    if len(input_list) < 2:
        print("List must have two elements to find the second largest.")
    else:
        
        largest = second_largest = float('-inf')
        
        for number in input_list:
            if number > largest: 
                second_largest = largest
                largest = number
                
            elif number > second_largest and number != largest:
                second_largest = number
                
        if second_largest == float('-inf'):
            print("No Second Largest element exists (all elements are the same.)")
            
        else:
            print(f'The second largest number is {second_largest}.')
            
except ValueError:
    print('Please enter a valid list of integers.')