# Last updated: 4/15/2025, 10:53:11 PM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def backtrack(i):
            # base case
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            backtrack(i+1) # Continue on

            subset.pop() # [1,2,3] -> [1,2] Consider options where we don't include
            backtrack(i+1)
        backtrack(0)
        return res