class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r = 0,len(s1) - 1
        temp = ''
        countS1 = collections.Counter(s1) # Hashmap of all letters inside s1
        while r <= len(s2) - 1:
            for i in range(l,r + 1):
                if s2[i] in countS1 and countS1[s2[i]] > 0:
                    countS1[s2[i]] -= 1
                else:
                    countS1 = collections.Counter(s1) # Reset counter
                    break 
            l += 1
            r += 1                                   
            if all([countS1[i] == 0 for i in countS1]):
                return True
        return False                   

                
                    
                
                
                