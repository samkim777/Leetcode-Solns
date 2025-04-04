class Solution:
    def isPalindrome(self, x: int) -> bool:
        back_x = 0
        orig = x

        while x > 0:
            back_x = back_x * 10 + x % 10
            x = x // 10
        
        return orig == back_x