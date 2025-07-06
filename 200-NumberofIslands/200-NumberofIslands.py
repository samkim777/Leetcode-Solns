# Last updated: 7/6/2025, 7:15:38 AM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        queue = deque()
        visited = set()
        numIslands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited: # Land
                    queue.append((r,c))
                    visited.add((r,c))
                    while queue:
                        row, col = queue.popleft()
                        for dr, dc in directions:
                            curRow, curCol = row + dr, col + dc
                            if curRow < rows and curRow >= 0 and curCol >= 0 and curCol < cols and grid[curRow][curCol] == "1" and (curRow,curCol) not in visited:
                                queue.append((curRow,curCol))
                                visited.add((curRow,curCol))
                    numIslands += 1
        return numIslands