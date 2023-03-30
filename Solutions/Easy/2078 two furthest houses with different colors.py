class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        l,r = 0, len(colors) - 1
        res = 1

        while l < r:
            if not colors[l] == colors[r]: # Different colored house
                res = max(res,r - l) # Save distance between two houses
                l += 1               # Increment left pointer
                r = len(colors) - 1  # Reset right pointer to end of list
            else: # House color same
                r -= 1               # Check by decrementing right pointer

        return res        # Return res
