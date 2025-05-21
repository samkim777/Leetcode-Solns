# Last updated: 5/21/2025, 1:00:23 AM
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digMap = {"2":"abc", "3":"def", "4":"ghi","5":"jkl", "6":"mno","7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        def backtrack(i,curStr):
            if i == len(digits):
                res.append(curStr)
                return
            
            for k in digMap[digits[i]]:
                backtrack(i+1,curStr+k)
        if not digits:
            return []
        backtrack(0,"")
        return res