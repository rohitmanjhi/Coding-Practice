import heapq

def kthElement(nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]

nums = [1,4,3,4,3,6,7]
highest = 2
print(kthElement(nums, highest))            
