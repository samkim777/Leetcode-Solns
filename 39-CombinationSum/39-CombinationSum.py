# Last updated: 5/3/2025, 11:08:25 PM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # only unique combinations
        # elements inside candidates is unique, so no need to worry about
        # duplicates
        res = []
        def backtrack(i, cur, curSum):
            # base case
            if target == curSum:
                res.append(cur.copy())
                return
            if i >= len(candidates) or target < curSum:
                return
            # include
            cur.append(candidates[i])
            backtrack(i, cur, curSum + candidates[i])
            
            # not include
            cur.pop()
            backtrack(i+1, cur, curSum)
        backtrack(0,[],0)
        return res