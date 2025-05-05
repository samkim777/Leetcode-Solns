# Last updated: 5/4/2025, 10:16:23 PM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # return all possible subsets
        res = []
        def backtrack(i, cur):
            if i >= len(nums):
                res.append(cur.copy())
                return
            # Decision to add
            cur.append(nums[i])
            backtrack(i+1, cur)

            # Not to add
            cur.pop()
            backtrack(i+1,cur)
        backtrack(0,[])
        return res