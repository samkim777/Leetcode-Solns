# Last updated: 6/29/2025, 7:35:02 AM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        
        def backtrack(i,cur):
            if i >= len(nums):
                res.append(cur.copy())
                return
            
            cur.append(nums[i])
            backtrack(i+1,cur)

            cur.pop()
            backtrack(i+1,cur)

        backtrack(0,[])
        return res
