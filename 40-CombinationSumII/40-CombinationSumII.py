# Last updated: 4/20/2025, 10:30:42 PM
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # riiiight you have to sort
        candidates.sort()
        res = []
        cur = []
        def backtrack(i,curSum):
            # base cases
            if target == curSum:
                res.append(cur.copy())
                return
            if i >= len(candidates) or target < curSum:
                return

            cur.append(candidates[i])
            backtrack(i+1, curSum + candidates[i])

            # No duplicates are allowed
            cur.pop()
            backIndex = i + 1
            while backIndex < len(candidates) and candidates[i] == candidates[backIndex]:
                backIndex += 1
            backtrack(backIndex ,curSum)
        backtrack(0,0)
        return res