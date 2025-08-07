# Last updated: 8/6/2025, 10:41:16 PM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i,cur):
            if i >= len(nums):
                res.append(cur.copy())
                return
            
            # Decision to add
            cur.append(nums[i])
            backtrack(i+1,cur)

            # Not add
            cur.pop()
            backtrack(i+1, cur)
        backtrack(0,[])
        return res