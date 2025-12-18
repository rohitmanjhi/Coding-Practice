def max_subarray_kadane(nums):
    if not nums:
        return ValueError("Input array cannot be None")

    max_sum = cur_sum = nums[0]

    for num in nums[1:]:
        cur_sum = max(num, cur_sum + num)
        max_sum = max(max_sum, cur_sum)
    return max_sum

print(max_subarray_kadane([-2,1,-3,4,-1,2,1,-5,4]))
