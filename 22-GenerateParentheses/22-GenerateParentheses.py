class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Conditions for backtracking:
        # 1) # Open Brackets < n
        # 2) # Closed Brackets < # Open Brackets
        # 3) Valid IIF # Closed Brackets == # Opem Brackets
        # Time: O(4n/sqrtn), Space: O(n)?
        res = []
        def backtrack(openN, closedN, sCur):
            if openN == closedN == n:
                res.append(sCur)
                return
            
            if openN < n:
                backtrack(openN + 1, closedN, sCur+"(")
            
            if closedN < openN:
                backtrack(openN, closedN + 1, sCur+")")
        backtrack(0,0,"")
        return res
