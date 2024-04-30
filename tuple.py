# Function returning multiple values using a tuple
def calculate_stats(numbers):
    return len(numbers), sum(numbers), min(numbers), max(numbers)

numbers = [10, 5, 8, 20, 3]
length, total, minimum, maximum = calculate_stats(numbers)
print("Length:", length)    # Output: 5
print("Total:", total)      # Output: 46
print("Minimum:", minimum)  # Output: 3
print("Maximum:", maximum)  # Output: 20
