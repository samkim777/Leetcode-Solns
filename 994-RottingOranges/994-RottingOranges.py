# Last updated: 6/17/2025, 10:31:04 PM
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        oranges = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: # Fresh
                    oranges += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        
        while queue and oranges:
            minutes += 1
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    curRow, curCol = row + dr, col + dc
                    if 0 <= curRow < rows and 0 <= curCol < cols and grid[curRow][curCol] == 1:
                        queue.append((curRow,curCol))
                        grid[curRow][curCol] = 2
                        oranges -= 1
        return minutes if oranges == 0 else -1