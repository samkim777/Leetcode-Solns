# Last updated: 5/10/2025, 10:55:08 PM
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(i, cur, curVal):
            if target == curVal:
                res.append(cur.copy())
                return
            if target < curVal or i >= len(candidates):
                return
            cur.append(candidates[i])
            backtrack(i + 1,cur, curVal + candidates[i])

            cur.pop()
            index = i + 1
            while index < len(candidates) and candidates[i] == candidates[index]:
                index += 1
            backtrack(index, cur, curVal)
        backtrack(0,[],0)
        return res