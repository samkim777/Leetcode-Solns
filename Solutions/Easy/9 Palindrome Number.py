class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringNum = str(x)
        l,r = 0, len(stringNum) - 1
        while l <= r:
            if stringNum[l] == stringNum[r]:
                l += 1
                r -= 1
            else: 
                return False
        return True            