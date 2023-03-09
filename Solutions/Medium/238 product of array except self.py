class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_products = [1] * n
        right_products = [1] * n
        output = [1] * n
        left_products[0] = 1
        right_products[n-1] = 1

        for i in range(1,len(nums)):
            left_products[i] = left_products[i-1] * nums[i-1]
        for j in range(len(nums) - 2,-1,-1):
            right_products[j] = right_products[j+1] * nums[j+1]

        for k in range(0,len(nums)):
            output[k] = left_products[k] * right_products[k]

        return output                    