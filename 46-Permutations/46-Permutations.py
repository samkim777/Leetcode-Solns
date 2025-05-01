# Last updated: 4/30/2025, 8:53:27 PM
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(cur):
            # base case
            if len(nums) == len(cur):
                res.append(cur.copy())
                return
            for num in nums:
                # If already seen skip
                if num in cur:
                    continue
                cur.append(num)
                backtrack(cur)
                # Pop and search other permutations
                cur.pop()
        backtrack([])
        return res