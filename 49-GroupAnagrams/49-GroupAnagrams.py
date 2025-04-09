# Last updated: 4/8/2025, 9:53:28 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary where the key is array of ascii values
        # Append all strings with the same array into that key
        # have the value for each key be an array itself
        # ** Remember that keys cannot be mutable in python
        group = defaultdict(list)
        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord('a') - ord(c)] += 1
            group[tuple(chars)].append(s)
        
        return list(group.values())
