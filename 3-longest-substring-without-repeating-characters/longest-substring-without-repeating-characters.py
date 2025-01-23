class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #"  " this is valid. 
        l,r = 0,0
        seen = set()
        res = 0
        while r < len(s):
            if s[r] in seen: # We've encountered a duplicate char
                seen.remove(s[l])
                l += 1
            else:
                seen.add(s[r])
                res = max(res, r - l + 1)
                r += 1
        return res        