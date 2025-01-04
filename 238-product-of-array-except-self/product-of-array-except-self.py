class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) time, and O(3n) --> O(n) space
        numLen = len(nums)
        postfix, prefix = [1] * numLen , [1] * numLen

        # prefix
        for i in range(1, numLen):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # postfix
        for j in range(numLen -2, -1 , -1):
            postfix[j] = postfix[j + 1] * nums[j + 1]
        
        results = [1] * numLen
        # results    
        for k in range(numLen):
            results[k] = postfix[k] * prefix[k]
        return results    