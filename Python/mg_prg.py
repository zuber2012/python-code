# Function to swap two numbers using a third variable
def swap_numbers(a, b):
    # Print initial values
    print(f"Before swapping: a = {a}, b = {b}")
    
    # Use a third variable to swap
    temp = a
    a = b
    b = temp
    
    # Print values after swapping
    print(f"After swapping: a = {a}, b = {b}")
    
    return a, b

# Test the function
a = 50
b = 100
a, b = swap_numbers(a, b)
