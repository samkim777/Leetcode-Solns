# Last updated: 5/2/2025, 10:47:44 PM
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = [False] * len(nums)
        def backtrack(cur):
            # base case
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                used[i] = True
                cur.append(nums[i])
                backtrack(cur)

                cur.pop()
                used[i] = False
        backtrack([])
        return res
