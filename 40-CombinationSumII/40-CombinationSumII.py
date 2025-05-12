# Last updated: 5/11/2025, 10:49:38 PM
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(i,curVal, curArr):
            # base case: Found target
            if target == curVal:
                res.append(curArr.copy()) # We add a shallow copy
                # since it is being passed through recursion
                return
            # target too small with current sum
            # index out of array
            if i >= len(candidates) or target < curVal:
                return
            # Decision to add
            curArr.append(candidates[i])
            backtrack(i+1, curVal + candidates[i], curArr)

            # Decision to not add
            curArr.pop()
            # Skip duplicate
            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(i+1, curVal, curArr)
            # we don't need to add curVal with another value because it'll 
            # recurse up anyways to handle when we follow "add" decision
        backtrack(0,0,[])
        return res