# Last updated: 5/1/2025, 11:25:50 PM
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        used = [False] * len(nums)
        def backtrack(cur):
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