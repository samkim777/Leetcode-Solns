class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count = [0] * 26
        s2Count = [0] * 26
        
        for i in range(len(s1)):
            s1Count[ord('a') - ord(s1[i])] += 1
            s2Count[ord('a') - ord(s2[i])] += 1

        for k in range(len(s2) - len(s1)):
            if s1Count == s2Count:
                return True
            s2Count[ord('a') - ord(s2[k])] -= 1
            s2Count[ord('a') - ord(s2[k+len(s1)])] += 1
        return s1Count == s2Count