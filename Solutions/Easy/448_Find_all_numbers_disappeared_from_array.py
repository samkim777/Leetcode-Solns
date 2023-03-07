class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        counter = {i: 0 for i in range(1, len(nums) + 1)}
        # Create dictionary of nums length with value
        # zeroes               
        res = []
        for i in nums: 
            if i not in counter: # i is not inside counter
                counter[i] = 0 # first occurence
            else: counter[i] += 1 # increase by 1

        for j in counter:
            if counter[j] == 0: # If we haven't seen
                res.append(j) # add to list

        return res              
