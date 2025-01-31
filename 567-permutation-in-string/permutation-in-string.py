class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Essentially idea is create a counter for s1, and a counter for length s1
        # that slides through s2. And then, as we iterate over s2, we add what ever
        # is on the right and removing what is on the left, and then comparing to s1 counter
        # O(N) time, O(1) space
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        # Slide over window s2
        for i in range(len(s2) - len(s1)):
            if s1Count == s2Count:
                return True
            s2Count[ord(s2[i]) - ord('a')] -= 1
            s2Count[ord(s2[i + len(s1)]) - ord('a')] += 1

        return s1Count == s2Count    