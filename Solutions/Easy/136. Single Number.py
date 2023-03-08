class Solution:
    def singleNumber(self, nums: List[int]) -> int:
       newdict = {i:0 for i in nums} # Initialize dictionary length nums      
       res = 0
       # Count occurence of items into dictionary
       for j in nums:
           if j not in newdict:
               newdict[j] = 0
           else: newdict[j] += 1
       # Check which one appears only once
       for k in newdict:
           if newdict[k] == 1:
               res = k
       # Return result
       return res   
