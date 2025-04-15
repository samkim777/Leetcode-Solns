# Last updated: 4/14/2025, 10:40:21 PM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        # Backtracking
        # Contraint: Current list of element is inside the results already
        # Goal: Return all possible subsets of list of integers
        # Ex: Given [1,2,3]: return [], [1],[2],[3],[1,2],[1,3],[2,1],[2,3],[3,1]... etc. Then filter out any duplicates
        def backtrack(index):
            if index >= len(nums):
                res.append(path.copy())
                return
            # Decision to add the cur number to list
            path.append(nums[index])
            backtrack(index + 1)

            # Decision to not add the cur number to list
            path.pop()
            backtrack(index + 1)    
        backtrack(0)
        return res              
