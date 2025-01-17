class Solution:
    def findMin(self, nums: List[int]) -> int:
        # include mid in the range because it could be the minimum
        # l < r if looking to narrow down range to an element
        # l <= r if looking for exact target
        l,r = 0, len(nums) - 1
        while l < r:
            mid = (l+r) // 2
            if nums[mid] >= nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]            