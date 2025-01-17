class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Intuition is that we know that if h = length of array
        # Then the minimum rate Koko should be eating these naners is 
        # the maximum value of the array
        # Hence, we can perform binary search on an array from 1 to this maximum
        # and find the maximum rate
        # O(logn) + O(n) thus O(n) time, O(1) space
        l,r = 1, max(piles)
        res = r
        while l <= r:
            k = (l+r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                res = min(k,res)
                r = k - 1
            else:
                l = k + 1    
        return res
