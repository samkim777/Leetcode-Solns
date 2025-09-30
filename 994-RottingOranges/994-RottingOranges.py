# Last updated: 10/1/2025, 12:42:24 AM
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        time = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    queue.append([row,col])
        # we have number of fresh oranges, rotten oranges
        # we also have a queue with rotten orange location
        # we can then traverse from there on our grid and per tick
        # change the fresh to rotten

        while fresh > 0 and queue:
            for i in range(len(queue)):
                row, col = queue.popleft() # rotten orange coords
                for dr,dc in directions: # traverse the grid 4 dirs
                    # if fresh orange add to queue
                    if row+dr < 0 or row+dr >= rows or col+dc < 0 or col+dc >= cols or grid[row+dr][col+dc] != 1:
                        continue
                    queue.append([row+dr,col+dc])
                    grid[row+dr][col+dc] = 2
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1