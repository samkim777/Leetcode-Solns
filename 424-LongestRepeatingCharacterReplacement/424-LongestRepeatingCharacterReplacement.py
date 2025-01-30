class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        count = {}
        max_frequency = 0
        max_length = 0

        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1 # Get current count or init 0

            max_frequency = max(max_frequency, count[s[r]])

            if (r - l + 1 - max_frequency) > k: # No more replacements can be made
                count[s[l]] -= 1
                l += 1

            max_length = max(max_length, r - l + 1)
            r += 1    
        return max_length
