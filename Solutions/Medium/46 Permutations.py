class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Permutations: [1,2,3]
        # [1,2,3] [1,3,2] [2,1,3] [2,3,1] [3,1,2], [3,2,1]
        # Order doesn't matter
        # Seems like a typical permutation tree 
        # Have a results list that will keep track of all the permutations
        res = []
        path = []
        # The backtracking algorithm will traverse each option, and obtain all possible permutations starting with that number. Afterwards, it will move onto the next integer
        def dfs(i):
            # Base case
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                dfs(i + 1)
                path.pop()
                

        dfs(0)
        return res        