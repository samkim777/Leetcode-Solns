# Last updated: 6/15/2025, 9:49:22 PM
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        rows, cols = len(isWater), len(isWater[0])
        queue = deque()
        res = [[-1] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    queue.append((r,c))
                    res[r][c] = 0

        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                curRow, curCol = dr + row, dc + col
                if 0 <= curRow < rows and 0 <= curCol < cols and res[curRow][curCol] == -1:
                    queue.append((curRow,curCol))
                    res[curRow][curCol] = res[row][col] + 1
        return res