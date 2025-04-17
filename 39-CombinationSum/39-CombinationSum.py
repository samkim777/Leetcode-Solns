# Last updated: 4/16/2025, 10:07:04 PM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # distinct integers candidates
        # target int
        # return LIST of all UNIQUE COMBINATIONS OF CANDIDATES 
        # WHERE sum equals TARGET
        # [2,3,6,7], target = 7
        # [[2,2,3], [7]]
        # but not [2,3,2], [3,2,2] etc
        res = []
        cur = []
        def backtrack(i, cur,curSum):
            # Base case
            if curSum == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or target < curSum:
                return
            
            cur.append(candidates[i])

            backtrack(i, cur,curSum + candidates[i])

            cur.pop()
            backtrack(i + 1, cur, curSum)
        backtrack(0,[],0)
        return res
            
            