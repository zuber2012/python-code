def unique_pairs(nums, target):
    seen = set()
    unique_pairs = set()
    
    for num in nums:
        complement = target - num
        if complement in seen:
            unique_pairs.add(tuple(sorted((num, complement))))
        seen.add(num)
    
    return sorted(list(unique_pairs))

# Test cases
print(unique_pairs([2, 7, 11, 15], 9))   # Output: [(2, 7)]
print(unique_pairs([1, 1, 2, 2, 3, 4, 5], 6))  # Output: [(1, 5), (2, 4)]
