# Last updated: 10/16/2025, 1:00:08 AM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        rows,cols = len(grid), len(grid[0])

        def dfs(r,c):
            # Base condition
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    res += 1
        return res
