# Last updated: 4/29/2025, 11:52:09 PM
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Given array of distinct integers return all possible permutations
        # [1,2,3] --> [1,2,3], [1,3,2]...
        # In essence, [1,2,3], then [1,2] then [1] then [1,3]...
        # backtrack([])
        # backtrack([1])
        # backtrack([1,2])
        # backtrack([1,2])
        # backtrack([1,2,3]) # return and save
        # backtrack([1,2])
        # backtrack([1]) # loop index at 3 so we do that
        # backtrack([1,3]) # recurse
        # backtrack([1,3,2])
        # backtrack([1,3])
        # backtrack([1])
        # backtrack([])
        # backtrack([2])... cont
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