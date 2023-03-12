class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = "".join(filter(lambda x:x.isalnum(), s)).lower() # Filter out any non number or alphabet
        length = len(word) - 1
        for i in range(0,len(word)):
            if word[i] != word[length]: # Two pointer traverse
                return False
            length -= 1
        return True             
            
        