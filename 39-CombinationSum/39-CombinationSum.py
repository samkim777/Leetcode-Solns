# Last updated: 5/7/2025, 10:22:53 PM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i,curSum,cur):
            if target == curSum:
                res.append(cur.copy())
                return
            if i >= len(candidates) or target < curSum:
                return
            
            cur.append(candidates[i])
            backtrack(i,curSum + candidates[i], cur)

            cur.pop()
            backtrack(i+1, curSum, cur)
        backtrack(0,0,[])
        return res