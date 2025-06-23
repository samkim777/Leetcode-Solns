# Last updated: 6/22/2025, 10:43:26 PM
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # Sort first so that when we make a decision to add or not to add,
        # we can skip accordingly. Does not affect overall time or space complexity
        candidates.sort()

        def backtrack(i, curVal, curArr):
            # Found
            if target == curVal:
                res.append(curArr.copy())
                return
            # Base case
            if i >= len(candidates) or target < curVal:
                return
            # Decision to add
            curArr.append(candidates[i])
            backtrack(i + 1, curVal + candidates[i], curArr)

            # Decision to skip
            # here we need to move our index accordingly so that we don't
            # add combinations with the same number twice
            # ex: [1,1,2] and [1,1,2] may use different numbers in terms of reference
            # but are same numbers
            curArr.pop()
            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i+= 1
            backtrack(i+1, curVal, curArr)
        backtrack(0,0,[])
        return res
