class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort
        nums.sort()
        res = []
        for i,a in enumerate(nums): #i index, a value
            if i > 0 and a == nums[i - 1]: #2nd value same as first
                continue
            l,r = i + 1, len(nums) - 1    
            while (l < r): 
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else: 
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1        
        return res               
                    