# Last updated: 4/24/2025, 9:21:20 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cur = {}
        for i, v in enumerate(nums):
            if target - v in cur:
                return [i, cur[target-v]]
            else:
                #9999
                cur[v] = i