# Last updated: 6/3/2025, 10:26:47 PM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i,cur):
            if i >= len(nums):
                res.append(cur.copy())
                return
            # decision to add
            cur.append(nums[i])
            backtrack(i+1, cur)

            cur.pop()
            backtrack(i+1, cur)
        backtrack(0,[])
        return res