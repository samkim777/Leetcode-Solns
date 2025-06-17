# Last updated: 6/16/2025, 9:16:28 PM
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        directions = [(1,0), (-1,0), (0,1),(0,-1)]
        rows, cols = len(isWater), len(isWater[0])
        queue = deque()
        result = [[-1] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    result[r][c] = 0
                    queue.append((r,c))

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                curRow, curCol = row + dr, col + dc
                # Check conditions
                if 0 <= curRow < rows and 0 <= curCol < cols and result[curRow][curCol] == -1:
                    queue.append((curRow,curCol))
                    result[curRow][curCol] = result[row][col] + 1
        return result