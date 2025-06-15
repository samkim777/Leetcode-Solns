# Last updated: 6/14/2025, 8:51:16 PM
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = deque()
        rows,cols = len(mat), len(mat[0])
        res = [[-1] * cols for _ in range(rows)]
        # Start bfs from 0s
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    res[r][c] = 0
                    queue.append((r,c))
        while queue:
            level_size = len(queue)
            row,col = queue.popleft()

            for r,c in directions:
                curRow = row + r
                curCol = col + c

                if 0 <= curRow < rows and 0 <= curCol < cols and res[curRow][curCol] == -1:
                    res[curRow][curCol] = res[row][col] + 1
                    queue.append((curRow,curCol))
        return res