class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # We can use two pointers / sliding window
        # If the left pointer >= right, increment left
        # If the right pointer > left, calculate current price, decrement right
        # return the result
        # O(n) time complexity, O(1) space, no extra used
        res = 0
        l,r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                res = max(res, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return res        
                   