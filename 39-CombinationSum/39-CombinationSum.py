# Last updated: 5/29/2025, 10:05:12 PM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i,curSum,cur):
            if target == curSum:
                res.append(cur.copy())
                return
            
            if target < curSum or i >= len(candidates):
                return
            
            cur.append(candidates[i])
            backtrack(i, curSum + candidates[i], cur)

            cur.pop()
            while i > 0 and candidates[i] == candidates[i-1]:
                i += 1
            backtrack(i+1, curSum, cur)

        backtrack(0,0,[])
        return res