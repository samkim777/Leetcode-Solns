class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l,r = 0,0
        res = 0
        while r < len(s):
            if s[r] not in seen: # If we've never seen, add and continue
                seen.add(s[r])
                res = max(res, r - l + 1)
                r += 1
            else: # Else if we've seen this current character before, increment left pointer
                while s[r] in seen:
                    # abcc
                    seen.remove(s[l])
                    l += 1
        return res        
