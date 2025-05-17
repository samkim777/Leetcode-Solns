# Last updated: 5/16/2025, 10:16:46 PM
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Partition a string s such that every substring of the partition
        # is a palindrome
        # ex) "aab" --> [["a","a","b"], ["aa","b"]]
        # the character itself is a palindrome
        # s = "abc"
        # [["a" "b" "c"]]
        # s = "aba"
        # [["a" "b" "a"], ["aba"]]
        res = []

        def isPalindrome(c):
            # logic for checking if palindrome
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

            for j in range(i,len(s)):
                if isPalindrome(s[i:j+1]):
                    curArr.append(s[i:j+1])
                    backtrack(j+1, curArr)
                    curArr.pop()
        backtrack(0,[])
        return res
                
        