class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix[i] = nums[i-1] * prefix[i-1]
        # postfix[i] = nums[i+1] * postfix[i+1]
        # result[i] = prefix[i] * postfix[i]
        nLen = len(nums)
        postfix, prefix = [1] * nLen, [1] * nLen
        for i in range(1,len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # postfix
        for j in range(len(nums) - 2, -1, -1): # R -> L
            postfix[j] = postfix[j + 1] * nums[j + 1]

        result = []    
        for k in range(len(nums)):
            cur = postfix[k] * prefix[k]
            result.append(cur)
        return result    