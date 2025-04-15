# Last updated: 4/14/2025, 10:56:22 PM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def backtrack(i):
            # base condition
            if i >= len(nums):
                res.append(subset.copy())
                return  
            subset.append(nums[i])
            backtrack(i+1)

            subset.pop()
            backtrack(i+1)
        backtrack(0)
        return res