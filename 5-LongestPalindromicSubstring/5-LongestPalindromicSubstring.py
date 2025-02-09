class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        longest = s[0]
        # At least two items
        for n in range(len(s) - 1):
            # even
            l,r = n,n+1
            while l >=0 and r < len(s) and s[l] == s[r]: # check for palindrome
                if (r - l + 1) > len(longest):
                    longest = s[l:r+1]
                l -= 1
                r += 1
            # Odd
            l, r = n,n
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(longest):
                    longest = s[l:r+1]
                l -= 1
                r += 1        
        return longest          
