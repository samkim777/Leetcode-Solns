class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # We could use a sliding window
        # while this current substring does not have repeating chars
        # get the length of the window, else start our window again
        # Loop through once, so O(n) time, constant space
        res = 0
        l,r = 0,0
        seen = set()
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                res = max(res, r - l + 1)
                r += 1
            else: # If we've seen
                seen.remove(s[l])
                l += 1
        return res        
                