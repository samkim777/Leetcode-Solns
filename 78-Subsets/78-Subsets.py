# Last updated: 4/14/2025, 11:08:39 PM
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
            backtrack(i+1)

            subset.pop()
            backtrack(i+1)
        backtrack(0)
        return res