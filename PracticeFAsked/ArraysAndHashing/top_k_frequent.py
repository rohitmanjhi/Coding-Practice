input = [1,1,2,3,3,3]

def top_k_frequent(nums, k):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    res = sorted(freq, key=lambda x:freq[x], reverse=True )    
    return res[:k]

print(top_k_frequent(input, 1))

from collections import Counter

def top_k_frequent_counter_through(nums, k):
    freq  = Counter(nums)

    res = [num for num, _ in freq.most_common(2)]
    return res

print(top_k_frequent_counter_through(input, 2))
