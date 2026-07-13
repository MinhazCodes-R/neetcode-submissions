class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        curr_num,prev,index_here = nums[0],None,0

        while nums[index_here] != -1:
            curr_num = nums[index_here]
            nums[index_here] = -1
            index_here = curr_num

        return index_here
        