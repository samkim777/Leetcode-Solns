# Last updated: 6/21/2025, 10:35:50 PM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking
        # Time complexity: O(??)
        # space complexity: O(??)
        res = []
        def backtrack(i,curVal,curArr):
            # Base case
            if i >= len(candidates) or target < curVal:
                return
            # Found 
            if target == curVal:
                res.append(curArr.copy())
                return
            
            # Decision to add
            curArr.append(candidates[i])
            backtrack(i, curVal + candidates[i], curArr)

            # Decision to not add
            curArr.pop()
            backtrack(i+1, curVal, curArr)
        backtrack(0,0,[])
        return res