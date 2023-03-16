class Solution:
    def maxArea(self, height: List[int]) -> int:
                      #          [1,8,6,2,5,4,8,3,7]
                      #          [8,8,7,6,5,4,3,2,1]
        res = []
        l,r = 0, len(height) - 1
        while (l < r):
            res.append(min(height[l],height[r]) * (r-l))
            if height[l] < height[r]: # Move the smaller pointer
                l += 1
            else: r -= 1
        res = max(res)         
        return res