class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Perhaps we could use hashset / hashmap
        # [1,2,2] target = 3 
        # [1,4,2,3] target = 5
        left = 0
        right = len(numbers) - 1   
        result = []


        while (left < right) :
            if numbers[left] + numbers[right] == target:
                result.append(left + 1)
                result.append(right + 1)
                break 
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else: 
                left +=  1                 
        return result        