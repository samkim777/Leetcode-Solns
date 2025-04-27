# Last updated: 4/26/2025, 10:56:09 PM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Given array nums of unique elements, return all possible subsets
        # soln set must not contain duplicates
        # ex) given nums = [1,2,3]
        # return [[], [1], [2], [1,2]]...
        # Decision tree: Include 1 or not include 1
        # include 2 or not include 2
        # include 3 or not include 3
        # use dfs
        res = []
        def dfs(i, cur):
            # base case:
            if i >= len(nums):
                res.append(cur.copy()) # copy to avoid messing with current array
                return
            # decision to add
            cur.append(nums[i])
            dfs(i+1, cur)

            cur.pop()
            dfs(i+1, cur)
        dfs(0,[])
        return res