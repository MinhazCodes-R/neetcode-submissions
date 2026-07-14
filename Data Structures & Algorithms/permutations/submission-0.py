class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        all_permutations = []
        combinations = []
        visisted_values = set()
        '''
        you pass down the combination arr and a set
        '''
        def dfs():
            nonlocal all_permutations, combinations, visisted_values, nums

            if len(visisted_values) == len(nums):
                all_permutations.append(combinations[:])
                return

            for number in nums:
                if number in visisted_values: continue
                else:
                    combinations.append(number)
                    visisted_values.add(number)
                    dfs()
                    del combinations[-1]
                    visisted_values.discard(number)
        dfs()
        return all_permutations

                



            
        