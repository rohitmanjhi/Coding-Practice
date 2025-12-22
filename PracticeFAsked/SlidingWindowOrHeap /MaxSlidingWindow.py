from collections import deque

def maxSlidingWindow(nums, k):
    # This deque will store INDEXES of useful elements
    dq = deque()

    # This list will store our final answers
    answer = []

    # Loop through each index of the array
    for i in range(len(nums)):

        # STEP 1:
        # Remove indexes that are OUTSIDE the current window
        # Current window is from (i - k + 1) to i
        if dq and dq[0] <= i - k:
            dq.popleft()

        # STEP 2:
        # Remove elements from the back that are SMALLER
        # than the current element
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # STEP 3:
        # Add current index to deque
        dq.append(i)

        # STEP 4:
        # Start saving maximums once the first window is complete
        if i >= k - 1:
            answer.append(nums[dq[0]])

    return answer


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

print(maxSlidingWindow(nums,k))
