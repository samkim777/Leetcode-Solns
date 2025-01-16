class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # if h = len(piles), that means k will be the maximum value
        # within the pile
        # Using this intuition, if we create an array from
        # 1 - max(piles), and use binary search to find the number
        # That divides eating speed into correct hours

        l,r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            # We'll need to iterate this found value and divide piles
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                res = min(k,res)
                r = k - 1
            else:
                l = k + 1
        return res        