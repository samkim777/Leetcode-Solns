# Last updated: 5/17/2025, 11:19:56 PM
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # permutation problem
        # create a map of digit to character
        # backtrack and form letter combinations of length digits
        # base case is when we went through entire list
        # Time: O(n^2), space: O(n), where n is length of digits
        res = []
        nums = {"2":"abc", "3":"def", "4":'ghi', "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        def permute(i, curStr):
            if i == len(digits):
                res.append(curStr)
                return
            for j in nums[digits[i]]:
                permute(i+1,curStr + j)
        if not digits:
            return []
        permute(0,"")
        return res