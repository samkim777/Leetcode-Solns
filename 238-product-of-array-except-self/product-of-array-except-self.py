class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix[i] = nums[i-1] * prefix[i-1]
        # postfix[i] = nums[i+1] * postfix[i+1]
        # result[i] = prefix[i] * postfix[i]
        # O(n) time, O(n) space
        nLen = len(nums)
        prefix = [1] * nLen
        for i in range(1,len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        postfix = 1    
        for k in range(len(nums) - 1, - 1, -1):
            prefix[k] *= postfix
            postfix *= nums[k]

        return prefix