class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = Counter(magazine) # Built in countuh, allows dups
        ran = Counter(ransomNote)
        for i in ran:
            if mag[i] < ran[i] or i not in mag:
                return False
        return True            