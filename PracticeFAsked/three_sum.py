from unittest import result


def three_sum(nums):
    nums.sort()
    res = []
    n = len(nums)

    for i in range(n-2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # duplicate skip
        l = i+1
        r = n-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s==0:
                res.append([nums[i] , nums[l] , nums[r]])
                l += 1
                r -= 1
            elif s<0:
                l +=1
            else:
                r -=1
    return res                


input = [-1, 0, 1, 2, -1, -4]
print(three_sum(input))
