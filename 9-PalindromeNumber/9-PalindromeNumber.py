class Solution:
    def isPalindrome(self, x: int) -> bool:
        l,r = 0, len(str(x)) - 1
        sInt = str(x)
        while l <= r:
            if sInt[l] != sInt[r]:
                return False
            l += 1
            r -= 1
        return True