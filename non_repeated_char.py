from collections import Counter

def first_non_repeated_char(word):
    counter = Counter(word)
    for char in word:
        if counter[char] == 1:
            return char
    return None
    
# Example usage
s = "abcrabck"
print(first_non_repeated_char(s))  # Output: 'r'
