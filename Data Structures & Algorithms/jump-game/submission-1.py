class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1 : return True
        end_value = len(nums)-1
        nums[len(nums)-1] = -1

        for i in range(len(nums)-2,-1,-1):
            # set -1 to possible and -2 to impossible
            if i + nums[i] >= end_value:
                end_value = i
        

        if nums[0] >= end_value: return True
        return False

           
        