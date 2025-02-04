class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cur = {}

        for i, v in enumerate(nums):
            if target - v in cur:
                return [i, cur[target-v]]
            else:
                cur[v] = i