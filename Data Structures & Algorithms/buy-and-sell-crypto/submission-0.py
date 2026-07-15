class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left_min = prices[0]
        for pivot in range(len(prices)):

            left_min = min(left_min,prices[pivot])
            max_profit = max(prices[pivot]-left_min,max_profit)

        return max_profit


        