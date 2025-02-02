class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Use a sliding window
        # use a hashmap
        max_freq = 0
        max_length = 0
        count = {}
        l,r = 0,0
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1

            max_freq = max(max_freq, count[s[r]])

            if (r - l + 1 - max_freq) > k: # no more replacements possible
                count[s[l]] -= 1
                l += 1

            max_length = max(max_length, r - l + 1)
            r += 1
        return max_length
