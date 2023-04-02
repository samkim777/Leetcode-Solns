class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        # If the current number is not a zero, then move pointer by 1 
        # Else add 1 to result variable
        res = 0
        l = 0
        while l < len(s):
            zeros,ones = 0,0
            while l < len(s) and s[l] == '0': # Found zero
                zeros += 1
                l += 1

            while l < len(s) and s[l] == '1': # Found one
                ones += 1
                l += 1
            res = max(res,min(zeros,ones) * 2)       
        return res            
                

                
                    
                
                
                