from itertools import permutations

# Function to find the second largest number in a list
def second_largest(numbers):
    unique_numbers = list(set(numbers))  # Remove duplicates
    unique_numbers.sort(reverse=True)    # Sort in descending order
    return unique_numbers[1] if len(unique_numbers) >= 2 else None  # Return second largest

# Function to rotate a list by k positions
def rotate_list(lst, k):
    k = k % len(lst)  # Handle cases where k is larger than list length
    return lst[-k:] + lst[:-k]  # Rotate list

# Function to flatten a nested list
def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))  # Recursively flatten
        else:
            flat_list.append(item)  # Append non-list item
    return flat_list

# Function to find all pairs in a list with a given sum
def find_pairs(lst, target_sum):
    pairs = []
    seen = set()
    for num in lst:
        complement = target_sum - num
        if complement in seen:
            pairs.append((complement, num))  # Add pair to result
        seen.add(num)  # Add number to seen set
    return pairs

# Function to find the length of the longest increasing subsequence in a list
def longest_increasing_subsequence(nums):
    if not nums:
        return 0  # Return 0 for empty list

    dp = [1] * len(nums)  # Initialize DP array
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)  # Update DP value
    return max(dp)  # Return maximum value in DP array

# Function to generate all permutations of a list
def all_permutations(lst):
    return list(permutations(lst))  # Generate permutations

# Function to find the most frequent element(s) in a list
def most_frequent(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1  # Increment frequency
        else:
            frequency[item] = 1  # Initialize frequency
    max_frequency = max(frequency.values())
    most_frequent_elements = [key for key, value in frequency.items() if value == max_frequency]  # Find max frequency elements
    return most_frequent_elements

# Function to perform zigzag conversion of a list
def zigzag_conversion(lst, numRows):
    if numRows == 1 or numRows >= len(lst):
        return lst  # Return original list if no zigzag needed

    zigzag = [[] for _ in range(numRows)]
    index, step = 0, 1

    for char in lst:
        zigzag[index].append(char)  # Add character to zigzag row
        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1
        index += step  # Move to next row

    return [item for sublist in zigzag for item in sublist]  # Flatten zigzag list

# Sample data for testing
numbers = [10, 20, 4, 45, 99, 99]
lst = [1, 2, 3, 4, 5]
nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
target_sum = 7
nums = [10, 9, 2, 5, 3, 7, 101, 18]
lst_perm = [1, 2, 3]
freq_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
zigzag_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
numRows = 3

# Function calls for demonstration with individual print statements
print("Second Largest Number:", second_largest(numbers))
print("Rotated List:", rotate_list(lst, 2))
print("Flattened List:", flatten(nested_list))
print("Pairs with sum", target_sum, ":", find_pairs(lst, target_sum))
print("Length of Longest Increasing Subsequence:", longest_increasing_subsequence(nums))
print("All Permutations:", all_permutations(lst_perm))
print("Most Frequent Element(s):", most_frequent(freq_list))
print("Zigzag Conversion:", zigzag_conversion(zigzag_list, numRows))
