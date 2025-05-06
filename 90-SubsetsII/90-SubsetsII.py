# Last updated: 5/5/2025, 10:37:44 PM
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        visited = [False] * len(nums)
        res = []
        def backtrack(i,cur):
            if i >= len(nums):
                res.append(cur.copy())
                return
            cur.append(nums[i])
            backtrack(i+1, cur)

            cur.pop()

            while i < len(nums) -1 and nums[i] == nums[i + 1]:
                i +=1
            backtrack(i + 1, cur)
        backtrack(0,[])
        return res

