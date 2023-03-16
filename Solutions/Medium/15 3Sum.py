class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       # Sort numbers in ascending order
        nums.sort()
        res = [] # result list
        for i,a in enumerate(nums): #index i and value a 
            if i > 0 and a == nums[i-1]: # Duplicate number
                continue
            else:
                l,r = i+1,len(nums) - 1
                while (l < r): # Two pointer
                    curSum = nums[i] + nums[l] + nums[r]
                    if curSum > 0: 
                        r -= 1
                    elif curSum < 0:
                        l += 1
                    else:
                        res.append([nums[i],nums[l],nums[r]])
                        l+=1  ## At this point l < r might be false
                        # but if the left pointer also pointing at duplicate
                        # iterate again
                        while (nums[l] == nums[l-1] and l < r): ## check again
                            l+=1              
        return res                            
                    