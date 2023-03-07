class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numset = set(nums) # Time complexity O(n), O(n) space 
        resultset = set()
        nums.sort() # Sort ascending order, O(nlogn) complexity on avg
        i=0
        while (i < len(nums) + 1): 
            resultset.add(i)    #O(n) 
            i+=1
        
        
        return sorted(resultset.difference(numset))[0] #O(1) since always one item
        # Over all time complexity O(nlogn)
## Using built in 

## More efficient
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(0,len(nums)):
            res += (i - nums[i])
        return res    