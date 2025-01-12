class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        res = []
        row, col = len(grid), len(grid[0])
        for r in range(row):
            if (r % 2 == 0): # 0,2,4 even rows, do even columns
                for c in range(col):
                    if c % 2 == 0: # even columns
                        res.append(grid[r][c])
            else: # odd rows, 0,1,3, do odd columns right to left 
                for cr in range(col-1,-1,-1):
                    if cr % 2 != 0: # odd column
                        res.append(grid[r][cr])
        return res            