class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxprofit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                maxprofit = max(maxprofit, abs(prices[l] - prices[r]))
            else:
                l = r
            r += 1    
        return maxprofit        