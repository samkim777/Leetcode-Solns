# Last updated: 5/16/2025, 10:38:42 PM
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(c):
            l,r = 0, len(c) - 1
            while l <= r:
                if c[l] != c[r]:
                    return False
                l += 1
                r -= 1
            return True
            
        def backtrack(i,curArr):
            if i >= len(s):
                res.append(curArr.copy())
                return
            for k in range(i,len(s)):
                if isPalindrome(s[i:k+1]):
                    curArr.append(s[i:k+1])
                    backtrack(k+1,curArr)
                    curArr.pop()
        backtrack(0,[])
        return res