class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # [100,4,200,1,3,2] to {100,4,200,1,3,2}
                           # If duplicates, [0,0,2,3] -> [0,2,3]
        longest = 0

        for n in nums:
            # Find the start of the sequence
            if (n - 1) not in numSet: 
                length = 0
                # Track with increasing length, the consecutive sequence length  
                while (n + length in numSet): 
                    length+=1
                longest = max(length,longest) 
        return longest             
