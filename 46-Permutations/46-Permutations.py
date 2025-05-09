# Last updated: 5/8/2025, 10:41:39 PM
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # permutations, order doesn't matter
        # no duplicates
        res = []
        def backtrack(i,cur):
            if len(nums) == len(cur):
                res.append(cur.copy())
                return
            if i >= len(nums):
                return
            for n in nums:
                if n in cur:
                    continue
                cur.append(n)
                backtrack(i+1,cur)

                cur.pop()
                backtrack(i+1, cur)
        backtrack(0,[])
        return res