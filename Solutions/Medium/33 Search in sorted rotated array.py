class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # integer array sorted in ascending order
        # No duplicate values
        # At some pivot index, the value at the pivot index
        # is rotated such that it becomes the first indexed item
        # inside our list
        # Given the array after rotation, and some integer target,
        # return the INDEX of target, if it is in nums, or -1 if not
        # Algorithm must run in O(log n)
        # pivot index at least 1, at most nums.length
        # The first element in list cannot be a pivot
        # Brute force way:
        # 1) for loop, iterate over every value, return -1 if not found
        # return index of target if found: O(n)
        # 2) if target in nums, then return its index: O(n)
        l,r = 0,len(nums) - 1
        res = -1
        while(l <= r):
            mid = (l + r) // 2
            if nums[mid] == target:
              res = mid
              break     

            if nums[mid] >= nums[l]: # left sorted
              if target < nums[l] or target > nums[mid]: # search right
                l = mid + 1
              else: 
                r = mid - 1  
            else:
              # Right sorted
              if target > nums[r] or target < nums[mid]:
                r = mid -1
              else: 
                l = mid + 1    
        return res  