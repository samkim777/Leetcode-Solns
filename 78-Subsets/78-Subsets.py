# Last updated: 4/18/2025, 9:57:55 PM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i, subset):
            # base case
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            backtrack(i+1, subset) # Continue on

            subset.pop() # [1,2,3] -> [1,2] Consider options where we don't include
            backtrack(i+1, subset)
        backtrack(0, [])
        return res