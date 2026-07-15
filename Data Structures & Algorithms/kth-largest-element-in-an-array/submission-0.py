class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #n*log(k) + klog(k)

        max_heap = []
        heapq.heapify(max_heap)
        for number in nums:
            heapq.heappush(max_heap,-number)
   
        val = None

        for i in range(k):

            val = -heapq.heappop(max_heap)

        return val
        