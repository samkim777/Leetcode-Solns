class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [3,2,1,6,3,8]
        res = 0
        l,r = 0, 1
        while r < len(prices):
            if prices[l] >= prices[r]: # too big, increment
                l = r
            else: # calculate profit
                res = max(res, prices[r] - prices[l])
            r += 1

        return res    