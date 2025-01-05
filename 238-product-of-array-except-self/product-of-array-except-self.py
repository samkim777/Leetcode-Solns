class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) time, and O(3n) --> O(n) space
        numLen = len(nums)
        postfix, prefix = [1] * numLen , [1] * numLen

        # prefix
        for i in range(1, numLen):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # do it in-place
        postfix = 1
        for k in range(numLen - 1, -1 ,-1):
            prefix[k] *= postfix
            postfix *= nums[k]

        return prefix    