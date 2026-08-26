class Solution:
    def rob(self, nums: List[int]) -> int:

        if (len(nums)==0):
            return 0
        elif (len(nums)==1):
            return nums[0]

        elif(len(nums)==2):
            return max(nums[0],nums[1])

        def rob_func(start,end):
            prev_1 = 0
            prev_2 = 0
            for i in range(start-1,end-1,-1):
                curr = max(nums[i]+prev_2,prev_1)
                prev_2 = prev_1
                prev_1 = curr


            return prev_1
        
        return(max(
            rob_func(len(nums),1),
            rob_func(len(nums)-1,0))
            )
        