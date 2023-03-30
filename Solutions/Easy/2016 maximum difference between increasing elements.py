class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        l,r = 0,1
        res = -1 # Return -1 if not found
        while r < len(nums): # sliding window until end of list
            if nums[l] >= nums[r]: # If left number >= right
                r += 1             # Increment right by 1
                l = r - 1          # Replace left to right pointer - 1
            else:
                res = max(res,abs(nums[l] - nums[r])) # Return biggest diff
                r += 1 # Iterate right pointer
        return res     # Return res