# Last updated: 4/18/2025, 10:01:47 PM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        def backtrack(i, curSum):
            # base case:
            # if i >= len(candidates), no feasible soln
            if i >= len(candidates) or curSum > target:
                return
            if curSum == target:
                res.append(cur.copy())
                return
            # Add cur index number and continue
            cur.append(candidates[i])
            backtrack(i, curSum + candidates[i])

            # Ah shiet we fked up, let's backtrack and pop the value
            cur.pop()
            backtrack(i+1, curSum) # this will go up and calculate cursum
        backtrack(0,0)
        return res