# Last updated: 5/18/2025, 11:46:44 PM
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Objective: Given string, return subsets of the string
        # such that each subset contains characters that are palindromes
        # aab --> [a a b] [aa b]
        # Time: O(n*2^n), space: O(n)
        res = []
        def isPalindrome(char):
            l,r = 0, len(char) - 1
            while l <= r:
                if char[l] != char[r]:
                    return False
                l += 1
                r -= 1
            return True
        def backtrack(i,cur):
            if i >= len(s):
                res.append(cur.copy())
                return
            for c in range(i,len(s)):
                if isPalindrome(s[i:c+1]): # 
                    cur.append(s[i:c+1])
                    backtrack(c+1, cur)
                    cur.pop()
        backtrack(0,[])
        return res