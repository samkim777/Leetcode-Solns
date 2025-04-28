# Last updated: 4/27/2025, 10:38:51 PM
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # To properly construct the combination sum
        # we need to handle duplicate values in the array before
        # we construct the decision tree
        # We do so by sorting the array
        candidates.sort()
        res = []
        # [1,1,2,5,6,7,10]
        def backtrack(i,cur, curVal):
            if target == curVal:
                res.append(cur.copy())
                return
            if i >= len(candidates) or target < curVal:
                return
            # Include decision
            cur.append(candidates[i])
            backtrack(i + 1, cur, curVal + candidates[i])
            # Decision to not include
            cur.pop()
            index = i + 1
            while index < len(candidates) and candidates[i] == candidates[index]:
                index += 1
            backtrack(index,cur, curVal)
        backtrack(0,[],0)
        return res