# Last updated: 10/6/2025, 4:57:55 PM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Time complexity : O(m*n)
        # Space complexity: O(m*n)
        queue = deque()
        islands = 0
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    queue.append((row,col))
                    grid[row][col] = "0"
                    while queue:
                        r,c = queue.popleft()
                        for dr,dc in directions:
                            curRow,curCol = r+dr,c+dc
                            if 0 <= curRow < rows and 0 <= curCol < cols and grid[curRow][curCol] == "1":
                                queue.append([curRow,curCol])
                                grid[curRow][curCol] = "0"
                    islands += 1
        return islands
            