# Last updated: 6/17/2025, 10:30:30 PM
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        directions = [(1,0), (-1,0), (0,-1), (0,1)]
        rows,cols = len(grid), len(grid[0])
        fresh_oranges = 0
        time = 0
        queue = deque()
        
        # First find position of rotten oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        
        while queue and fresh_oranges > 0:
            time += 1
            level_size = len(queue)

            # Check the 4 directions from currently rotten oranges
            for _ in range(level_size):
                row, col = queue.popleft()

                for dr, dc in directions:
                    curRow = row + dr
                    curCol = col + dc

                    # Check within bounds and fresh
                    # don't need visited set because we are marking the grid as we traverse
                    if 0 <= curRow < rows and 0 <= curCol < cols and grid[curRow][curCol] == 1:
                        grid[curRow][curCol] = 2
                        fresh_oranges -= 1
                        queue.append((curRow,curCol))
        return time if fresh_oranges == 0 else -1

