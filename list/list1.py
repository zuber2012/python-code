# Question: How do you create a list in Python?
# Creating a list with five elements
my_list = [1, 2, 3, 4, 5]
# Printing the list
print(my_list)
# Output: [1, 2, 3, 4, 5]

# Question: How do you access elements in a list using indices?
my_list = [1, 2, 3, 4, 5]
# Accessing the first element
print(my_list[0])  # Output: 1
# Accessing the last element
print(my_list[-1]) # Output: 5

# Question: How do you update elements in a list?
my_list = [1, 2, 3, 4, 5]
# Updating the third element (index 2)
my_list[2] = 10
# Printing the updated list
print(my_list)  # Output: [1, 2, 10, 4, 5]


# Question: How do you append an element to a list?
my_list = [1, 2, 3, 4, 5]
# Appending the number 6 to the list
my_list.append(6)
# Printing the list after appending
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Question: How do you remove an element from a list?
my_list = [1, 2, 3, 4, 5]
# Removing the number 3 from the list
my_list.remove(3)
# Printing the list after removing
print(my_list)  # Output: [1, 2, 4, 5]

# Question: How do you pop (remove and return) the last element from a list?
my_list = [1, 2, 3, 4, 5]
# Popping the last element
popped_element = my_list.pop()
# Printing the popped element
print(popped_element)  # Output: 5
# Printing the list after popping
print(my_list)         # Output: [1, 2, 3, 4]

# Question: How do you square each number in a list using list comprehensions?
my_list = [1, 2, 3, 4, 5]
# Squaring each element in the list
squared_list = [x**2 for x in my_list]
# Printing the list of squared numbers
print(squared_list)  # Output: [1, 4, 9, 16, 25]

# Question: How do you filter even numbers from a list using list comprehensions?
my_list = [1, 2, 3, 4, 5, 6]
# Filtering even numbers
even_list = [x for x in my_list if x % 2 == 0]
# Printing the list of even numbers
print(even_list)  # Output: [2, 4, 6]

# Question: How do you filter even numbers from a list using list comprehensions?
my_list = [1, 2, 3, 4, 5, 6]
# Filtering even numbers
even_list = [x for x in my_list if x % 2 == 0]
# Printing the list of even numbers
print(even_list)  # Output: [2, 4, 6]

# Question: How do you concatenate two lists?
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# Concatenating list1 and list2
concatenated_list = list1 + list2
# Printing the concatenated list
print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]

# Question: How do you find the length of a list?
my_list = [1, 2, 3, 4, 5]
# Finding the length of the list
print(len(my_list))  # Output: 5

# Question: How do you find the sum of all elements in a list?
my_list = [1, 2, 3, 4, 5]
# Calculating the sum of the elements
total_sum = sum(my_list)
# Printing the sum
print(total_sum)  # Output: 15

# Question: How do you find the maximum and minimum elements in a list?
my_list = [1, 2, 3, 4, 5]
# Finding the maximum element
max_element = max(my_list)
# Finding the minimum element
min_element = min(my_list)
# Printing the max and min elements
print(f"Max: {max_element}, Min: {min_element}")  # Output: Max: 5, Min: 1

# Question: How do you flatten a nested list?
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
# Flattening the nested list
flat_list = [item for sublist in nested_list for item in sublist]
# Printing the flattened list
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Question: How do you transpose a matrix (2D list)?
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Transposing the matrix
transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# Printing the transposed matrix
print(transposed_matrix)  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Question: How do you remove duplicates from a list?
my_list = [1, 2, 2, 3, 4, 4, 5]
# Removing duplicates by converting to a set and back to a list
unique_list = list(set(my_list))
# Printing the list without duplicates
print(unique_list)  # Output: [1, 2, 3, 4, 5]

# Question: How do you find the intersection of two lists?
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
# Finding the intersection
intersection = [x for x in list1 if x in list2]
# Printing the intersection
print(intersection)  # Output: [3, 4]

# Question: How do you rotate a list by k elements?
def rotate_list(lst, k):
    # Rotating the list by slicing
    return lst[-k:] + lst[:-k]

my_list = [1, 2, 3, 4, 5]
# Rotating the list by 2 elements
rotated_list = rotate_list(my_list, 2)
# Printing the rotated list
print(rotated_list)  # Output: [4, 5, 1, 2, 3]

# Question: How do you find the second largest number in a list?
my_list = [1, 2, 3, 4, 5]
# Removing duplicates by converting to a set and back to a list
unique_list = list(set(my_list))
# Sorting the list
unique_list.sort()
# Finding the second largest element
second_largest = unique_list[-2]
# Printing the second largest element
print(second_largest)  # Output: 4

# Question: How do you split a list into even and odd numbers using list comprehensions?
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Splitting the list into even numbers
even_numbers = [x for x in my_list if x % 2 == 0]
# Splitting the list into odd numbers
odd_numbers = [x for x in my_list if x % 2 != 0]
# Printing the lists of even and odd numbers
print("Even numbers:", even_numbers)  # Output: Even numbers: [2, 4, 6, 8, 10]
print("Odd numbers:", odd_numbers)    # Output: Odd numbers: [1, 3, 5, 7, 9]






