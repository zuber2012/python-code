import re

def is_match(s1, s2):
    # Convert the custom pattern to a regex pattern
    regex_pattern = s2.replace('_', '.').replace('%', '.*')
    
    # Add anchors to match the entire string
    regex_pattern = '^' + regex_pattern + '$'
    
    # Use re.fullmatch to check if the entire s1 matches the pattern
    return re.fullmatch(regex_pattern, s1) is not None

# Examples
print(is_match("abc", "a"))       # Output: False
print(is_match("ba", "b_"))       # Output: True
print(is_match("abcdef", "_%"))   # Output: True
