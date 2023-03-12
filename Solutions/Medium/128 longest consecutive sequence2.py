class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # [100,4,200,1,3,2] to {100,4,200,1,3,2}
                           # If duplicates, [0,0,2,3] -> [0,2,3]
        longest = 0

        for n in nums:
            if (n - 1) not in numSet: # Start of sequence
                length = 0  
                while (n + length in numSet): #O(s), where s = length
                    length+=1
                longest = max(length,longest) # Keep track of longest
        return longest             
