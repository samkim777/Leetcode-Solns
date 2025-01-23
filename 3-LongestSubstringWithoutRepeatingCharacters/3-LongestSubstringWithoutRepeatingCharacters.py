class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # O(n) time and space complexity
        # Empty substring is considered a valid substring :shrug:
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
                