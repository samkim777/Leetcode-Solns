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

    # Faster solution without duplicate Counter()     
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r = 0,len(s1)
        countS1 = collections.Counter(s1) 
        while r <= len(s2):
          if countS1 == collections.Counter(s2[l:r]):
            return True
          l+= 1
          r+= 1
        return False    

    # optimal solution using ASCII Values

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Count, s2Count = [0] * 26, [0] * 26 #initialize hashmap length 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1 

        matches = 0

        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0

        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            index = ord(s2[r]) - ord('a') # Key of right pointer 
            s2Count[index] += 1 
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a') # Key of left pointer
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1 
            l += 1

        return matches == 26     
                                                 

                
                    
                
                
                