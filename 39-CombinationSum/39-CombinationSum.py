# Last updated: 4/17/2025, 10:45:07 PM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i,cur,curSum):
            # base case
            if curSum == target:
                res.append(cur.copy())
                return

            if i >= len(candidates) or curSum > target:
                return
            cur.append(candidates[i])
            backtrack(i,cur,curSum + candidates[i])

            cur.pop()
            backtrack(i + 1,cur, curSum)
        backtrack(0,[],0)
        return res