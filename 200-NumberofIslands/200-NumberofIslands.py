# Last updated: 10/14/2025, 11:58:18 PM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS immediately comes to mind with these 2D grid problems
        # When we meet land, then we can add that to our queue
        # And mark it as water to make sure we don't visit it again
        # Standard bfs approach
        # Time complexity will be O(m*n) because we must traverse the
        # entire grid
        # Space complexity will be O(m*n) because in worst case scenario
        # when we have all lands, our queue will be size of the grid
        # Assuming m,n >= 1
        queue = deque()
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        numIslands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1": # If watuh, add to queue
                    queue.append((r,c))
                    grid[r][c] = "0"
                    while queue:
                        row,col = queue.popleft() # get current land
                        for dr, dc in directions:
                            curRow, curCol = row + dr, col + dc
                            # Check validity
                            if curRow < 0 or curRow >= rows or curCol < 0 or curCol >= cols or grid[curRow][curCol] == "0":
                                continue
                            grid[curRow][curCol] = "0"
                            queue.append((curRow,curCol))
                    numIslands += 1
        return numIslands

