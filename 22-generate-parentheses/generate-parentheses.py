class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # add Open if # open < n
        # add closed if # closed < open
        # valid IIF open == closed == n
        # Time: O(4n/sqrt(n)), space: O(n)
        res = []
        def backtrack(openN, closedN, sPath):
            # Base
            if openN == closedN == n:
                res.append(sPath)
                return
            # Open < n
            if openN < n:
                backtrack(openN + 1, closedN, sPath+"(")    
             # closed < open
            if closedN < openN:
                backtrack(openN, closedN + 1, sPath+")")
        backtrack(0,0,"")
        return res 
