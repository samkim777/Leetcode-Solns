# Last updated: 6/6/2025, 10:42:31 PM
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Because our nums array contains duplicates, this means that
        # in our decision tree, the decision to not include an element
        # will require an extra step to ensure that we do not
        # contain duplicate power sets
        nums.sort()
        res = []

        def backtrack(i,cur):
            if i >= len(nums):
                res.append(cur.copy())
                return
            
            # decision tree to add
            cur.append(nums[i])
            backtrack(i+1, cur)

            # Decision to not add
            cur.pop()
            # We do not want to recurse if already used the number
            while i < len(nums)- 1 and nums[i] == nums[i + 1]:
                i+= 1
            backtrack(i+1, cur)
        backtrack(0,[])
        return res