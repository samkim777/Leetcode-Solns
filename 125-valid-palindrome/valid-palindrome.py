class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        strs = []
        for string in s:
            if string.isalnum():
                strs.append(string.lower())

        l,r = 0, len(strs) - 1
        while l < r:
            if strs[l] != strs[r]:
                return False
            l += 1
            r -= 1
        return True                



