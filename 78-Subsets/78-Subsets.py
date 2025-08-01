# Last updated: 7/31/2025, 10:10:34 PM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 2 decisions to make: To add the current number or to skip
        # 2^n time complexity
        # O(n) space complexity because worst case we have all the numbers added
        # in the current array
        res = []
        def backtrack(i,curArr):
            if i >= len(nums):
                res.append(curArr.copy()) # Return shallow copy so as to not mess with recursive variable call
                return
            # decision to add
            curArr.append(nums[i])
            backtrack(i+1,curArr)

            # decoision to skip
            curArr.pop() # Pops right most element
            backtrack(i+1,curArr)
        backtrack(0,[])
        return res