class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(tuple(s)) == sorted(tuple(t))      

        # Using python's built in tuple and sorted methods

        