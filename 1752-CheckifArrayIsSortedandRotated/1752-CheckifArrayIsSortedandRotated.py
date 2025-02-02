class Solution:
    def check(self, nums: List[int]) -> bool:
        # the equation nums[( index + x) % len(nums)]
        # is for circular array, which means at the end of the array
        # we will compare with the first element
        
        num_rotatable = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                num_rotatable += 1
        return num_rotatable <= 1