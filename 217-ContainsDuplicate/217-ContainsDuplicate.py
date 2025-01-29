class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()
        for i in nums:
            if i not in duplicate:
                duplicate.add(i)
            else:
                return True

        return False            