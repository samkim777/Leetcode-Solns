class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort in ascending order
        nums.sort()
        res = []
        cur = 0
        # -1,0,2,5
        for i in range(len(nums) - 2):
            # Dodge duplicates by checking if the number that we're currently seeing was already seen
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                threesum = nums[left] + nums[i] + nums[right]
                if threesum > 0:
                    right -= 1
                elif threesum < 0:
                    left += 1
                else:
                    res.append([nums[left],nums[i],nums[right]])
                    # Keep looking for more zero three sums
                    left += 1
                    # Once we've iterated and we find another duplicate, increment left pointer again
                    while (left < right and nums[left] == nums[left - 1]):
                        left += 1

        return res                                                   
                    