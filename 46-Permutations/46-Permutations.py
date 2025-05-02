# Last updated: 5/1/2025, 11:12:00 PM
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # In a decision tree,
        # Add 1, Then add 2 or 3, Then add 3 or 2
        # Add 2 Then add 1 or 3, then add 3 or 1
        # Add 3 Then add 1 or 2, then add 2 or 1
        # Use a for loop to loop over every number
        # Since permutation, O(n!) time, space is O(n)?
        res = []
        def backtrack(cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            for n in nums:
                if n in cur:
                    continue
                cur.append(n)
                backtrack(cur)

                cur.pop() # Try other permutations
        backtrack([])
        return res