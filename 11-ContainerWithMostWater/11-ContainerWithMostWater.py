class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Go through everything, keep track of maximum area?
        # if greater than or equal, increment/decrement the other
        # O(n) time, O(1) space
        l, r = 0, len(height) - 1
        maxArea = 0
        while l < r:
            curArea = min(height[l], height[r]) * (r - l)
            maxArea = max(maxArea, curArea)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return maxArea             