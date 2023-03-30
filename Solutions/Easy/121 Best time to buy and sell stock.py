class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if only one price given, then we return 0
        # Otherwise, we can check the first value of the list
        # against the second and determine the difference
        # We want the difference to be a negative number
        # If we get a negative number, calculate the difference
        # and store the absolute value of that as result
        # Continue down the list by iterating the right pointer
        # If we are at a positive number, then iterate left pointer 
        l,r = 0,1 # Initialize two pointers
        res = [0]
        while r < len(prices):
            if prices[l] - prices[r] <= 0:
                res.append(abs(prices[l] - prices[r]))
                r += 1
            else: 
                l += 1  
                
        return max(res)        
