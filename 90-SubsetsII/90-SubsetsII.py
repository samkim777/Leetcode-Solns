# Last updated: 5/6/2025, 10:05:47 PM
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # for subsets, since the order is linear, we can use
        # while loop to skip index instead of for loop ??
        res = []
        nums.sort() # have to sort for easier dup check
        def backtrack(i,cur):
            # base case
            if i >= len(nums):
                res.append(cur.copy())
                return
            
            # Decision to add
            cur.append(nums[i])
            backtrack(i+1, cur)

            cur.pop()
            # skip dupliactes
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i+1, cur)
        backtrack(0,[])
        return res