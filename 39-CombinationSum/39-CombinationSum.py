# Last updated: 4/28/2025, 9:42:27 PM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i,cur,curSum):
            if target == curSum:
                res.append(cur.copy()) # shallow copy to not mess with cur array being passed in
                return
            if i >= len(candidates) or curSum > target:
                return
            
            # choose to add
            cur.append(candidates[i])
            backtrack(i, cur,curSum + candidates[i])

            # Remove and backtrack
            cur.pop()
            backtrack(i+1, cur, curSum)
        backtrack(0,[],0)
        return res