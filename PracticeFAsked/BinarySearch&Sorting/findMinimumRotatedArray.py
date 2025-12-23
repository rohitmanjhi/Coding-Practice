from typing import List

def findMinimum(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] >= right:
            left = mid + 1
        else:
            right = mid 
    print(left, nums[left])        
    return nums[left]            
nums = [3,4,5,1,2]
print(findMinimum(nums))
