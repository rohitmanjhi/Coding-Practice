from collections import Counter

def find_duplicate(arr):
    counter = Counter(arr)
    for key, value in counter.items():
        if value > 1:
            return key
    return None

print(find_duplicate( [3, 4, 5, 6, 5]))
