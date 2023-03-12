class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        res = []
        nodup = set(nums)
        list_nums = list(nodup)
        list_nums.sort()

        i = 0
        if len(nums) == 0: return 0
        while i < len(list_nums) - 1:
            if list_nums[i] + 1 == list_nums[i+1]:
                count += 1
            else:
                res.append(count)
                count = 1
            i += 1

        res.append(count)
        return max(res) 