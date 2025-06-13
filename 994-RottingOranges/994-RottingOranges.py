# Last updated: 6/12/2025, 10:07:45 PM
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        queue = deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        rows,cols = len(grid), len(grid[0])
        minutes = 0
        fresh_oranges = 0

        # Find the rotten orange positions
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        
        while queue and fresh_oranges > 0:
            # Each iteration increments time by 1
            minutes += 1
            level_size = len(queue)

            for _ in range(level_size):
                r,c = queue.popleft()
                for dr, dc in directions:
                    curRow = dr + r
                    curCol = dc + c

                    # Check condition
                    if 0 <= curRow < rows and 0 <= curCol < cols and grid[curRow][curCol] == 1:
                        queue.append((curRow,curCol))
                        grid[curRow][curCol] = 2
                        fresh_oranges -= 1
        return minutes if fresh_oranges == 0 else -1

