class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Basic binary search algorithm
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1    
        res = -1
        l,r = 0, len(nums) - 1
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] > target: 
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                res = mid
                return res
        return res                