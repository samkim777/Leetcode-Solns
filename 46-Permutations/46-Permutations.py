# Last updated: 4/29/2025, 11:39:20 PM
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Given array of distinct integers return all possible permutations
        # [1,2,3] --> [1,2,3], [1,3,2]...
        # Can backtrack
        # decision tree to include element 0, not include
        # include element 1, not include... so on and so forth
        res = []
        def backtrack(cur):
            # base case, length of cur == length of nums
            if len(nums) == len(cur):
                res.append(cur.copy()) # shallow copy to avoid issues while recursing
                return
            for num in nums:
                if num in cur:
                    continue
                cur.append(num) # [1], [1,2], [1,2,3]
                backtrack(cur)
                cur.pop()
        backtrack([])
        return res