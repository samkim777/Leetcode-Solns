class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1

        for i in range(len(arr) - 1, -1, -1): # Loop backwards 
            newMax = max(right_max,arr[i]) # Compare current value and previous max to find the max so far
            arr[i] = right_max # Replace the current i'th array value with max
            right_max = newMax # Update max

        return arr    
            