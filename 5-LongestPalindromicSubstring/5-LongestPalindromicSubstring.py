# Last updated: 5/30/2025, 10:53:31 PM
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Check from forward to bmmmmmkm
        if len(s) == 1:
            return s
        longest = s[0]
        for n in range(len(s) - 1):
            # Odd
            l, r = n,n
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(longest):
                    longest = s[l:r+1]
                l -= 1
                r += 1 
            # even
            l,r = n,n+1
            while l >=0 and r < len(s) and s[l] == s[r]: # check for palindrome
                if (r - l + 1) > len(longest):
                    longest = s[l:r+1]
                l -= 1
                r += 1       
        return longest         
