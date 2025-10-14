# Last updated: 10/14/2025, 11:53:08 PM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        islands = 0

        def dfs(i,j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r,c)
        return islands