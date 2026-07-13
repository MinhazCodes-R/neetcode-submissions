class Solution:
    def rob(self, nums: List[int]) -> int:
        for i in range (len(nums)-1,-1,-1):

            num1 = nums[i]+(nums[i+2] if i+2<len(nums) else 0)
            num2 = nums[i+1] if i+1<len(nums) else 0

            nums[i] = max(num1,num2)
        
        return nums[0]
        