class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initial list is sorted in ascending order
        # Rotated 1 to n times, so always rotated at least once
        # Rotating by n times resets it to the inital list
        # [1,2,3,4,5] [5,2,3,4,1]
        # case where we rotated n times, and have the initial list
        # We will treat this case in special case
        # [3,4,5,1,2] Compare 3 and 5 
        # Since 5 is bigger than 3, it must be that up until this middle point, we must be increasing. And so search the right side of the list
        # [5,1,2,3,4] 2 is less than 5, so we move r pointer to mid - 1, ie
        # search the left side of the list
        l,r = 0, len(nums) - 1
        res = nums[0]
        while(l <= r):
            if nums[l] < nums[r]: # Initial array
                res = min(res,nums[l])
                break
            mid = (l + r) // 2
            res = min(res,nums[mid])
            if nums[mid] >= nums[l]: # If 2 elements, then rounds to 0, so need equal check 
                l = mid + 1 # l = nums[4] == 0
            else:
                r = mid - 1
        return res      