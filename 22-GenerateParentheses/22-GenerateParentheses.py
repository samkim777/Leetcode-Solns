class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # condition for valid parenthese:
        # open Brackets < closed Brackets
        # closed brackets < n
        # open brackets == closed brackets == n
        res = []

        def backtrack(openN, closedN, cur):
            if openN == closedN == n:
                res.append(cur)
                return
            
            if openN < n:
                backtrack(openN + 1, closedN, cur+"(")

            if closedN < openN:
                backtrack(openN, closedN + 1, cur+")")
        
        backtrack(0,0,"")
        return res