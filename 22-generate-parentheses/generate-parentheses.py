class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add closed parentheses if # closed < # open
        # only add open parentheses if # open < n
        # valid IIF open == closed == n
        res = []
        def backtrack(openN, closedN, sPath):
            # Base case
            if openN == closedN == n:
                res.append(sPath)

            # If we can add more open brackets, backtrack
            if openN < n:
                backtrack(openN + 1, closedN, sPath+"(")
            
            # else if we can only add closed brackets, backtrack
            if closedN < openN:
                backtrack(openN, closedN + 1, sPath+")")
                
        backtrack(0,0,"")
        return res