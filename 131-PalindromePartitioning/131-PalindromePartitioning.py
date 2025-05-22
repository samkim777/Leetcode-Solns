# Last updated: 5/21/2025, 11:44:26 PM
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(char):
            l,r = 0, len(char) - 1
            while l <= r:
                if char[l] != char[r]:
                    return False
                l+=1
                r -= 1
            return True
        def backtrack(i,cur):
            if i >= len(s):
                res.append(cur.copy())
                return
            for k in range(i,len(s)):
                if isPalindrome(s[i:k+1]):
                    cur.append(s[i:k+1])
                    backtrack(k+1,cur)
                    cur.pop()
        backtrack(0,[])
        return res