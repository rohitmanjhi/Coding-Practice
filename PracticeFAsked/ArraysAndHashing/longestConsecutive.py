
def longestConsecutive(nums):
    if not nums:
        return 0

    s = set(nums)
    longest = 0

    for num in nums:
        if num - 1 not in s:
            length = 1
            curr = num + 1
            while curr in s:
                length += 1
                curr += 1
            longest = max(length, longest) 
    return longest           


input = [100,4,200,1,3,2]

print(longestConsecutive(input))
