# Last updated: 4/19/2025, 5:05:23 PM
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() # skip duplicates
        res = []
        cur = []
        def backtrack(i,curSum):
            if target == curSum:
                res.append(cur.copy())
                return
            if target < curSum or i >= len(candidates):
                return

            cur.append(candidates[i])
            backtrack(i+1, curSum + candidates[i])

            cur.pop()
            # When we backtrack, we should not include the same number again
            # in our decision tree because otherwise we will include
            # duplicate combination sums
            # ie, [1,1,5] and [1,5,1]
            # So the way to skip it is to check if the next val duplicate
            # and keep incrementing pointer if so
            next_i = i + 1
            while next_i < len(candidates) and candidates[next_i] == candidates[i]:
                next_i += 1
            backtrack(next_i, curSum)
        backtrack(0,0)
        return res
