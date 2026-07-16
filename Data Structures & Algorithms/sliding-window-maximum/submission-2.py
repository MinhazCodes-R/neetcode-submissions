class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return_arr = []
        min_heap = []
        heapq.heapify(min_heap)

        for index,i in enumerate(nums):
            if index == k: break
            heapq.heappush(min_heap,(-i,index))

        return_arr.append(-min_heap[0][0])
        print(min_heap)

        for i in range(k,len(nums)):
            heapq.heappush(min_heap,(-nums[i],i))
            while min_heap[0][1]<=i-k:
                heapq.heappop(min_heap)
            return_arr.append(-min_heap[0][0])

        return return_arr


        