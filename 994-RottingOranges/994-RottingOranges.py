# Last updated: 7/5/2025, 7:17:05 AM
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        queue = deque()
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1), (0,-1)]
        visited = set()
        oranges = 0
        time = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    oranges += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
                    visited.add((r,c))

        while queue and oranges:
            time += 1
            for _ in range(len(queue)):
                row, col = queue.popleft() # rotten orange
                for dr, dc in directions:
                    if row + dr < rows and row + dr >= 0 and col + dc < cols and col + dc >= 0 and grid[row+dr][col+dc] == 1:
                        grid[row+dr][col+dc] = 2
                        oranges -= 1
                        queue.append((row+dr,col+dc))
                        visited.add((row+dr,col+dc))
        return time if oranges == 0 else -1
        
