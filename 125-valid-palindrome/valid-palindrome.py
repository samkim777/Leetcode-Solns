class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for string in s:
            if string.isalnum():
                res.append(string.lower())
        l,r = 0, len(res) - 1
        while l < r:
            if res[l] != res[r]:
                return False
            l += 1
            r -= 1
        return True                