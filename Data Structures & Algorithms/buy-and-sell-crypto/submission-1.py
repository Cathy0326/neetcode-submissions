class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(0, len(prices)):
            buy = prices[i]
            for j in range(i+1,len(prices)):
                sell = prices[j] - prices[i]
                res = max(res, sell)
        return res