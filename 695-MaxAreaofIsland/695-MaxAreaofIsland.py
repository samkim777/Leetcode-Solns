# Last updated: 10/14/2025, 12:44:43 AM
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # The immediate algorithm that comes to mind
        # is to use BFS, since we are dealing with 4 way direction check
        # where we have to check all 4 directions for something and bfs
        # is particularly useful for that
        # We could also use dfs I think, but I can't think off the top of 
        #my head how we'd approach it
        # If we go ahead with BFS, the time complexity would be
        # O(m*n), since in the worst case, the entire grid is one big island
        # and we'd have to add the entire grid while processing few
        # Space complexity is O(m*n), again same as reason above
        queue = deque()
        visited = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: # found island
                    queue.append((r,c))
                    grid[r][c] = 0
                    cur_size = 0
                    while queue:
                        row, col = queue.popleft() # Get the island coord
                        cur_size += 1 # increment current island size
                        for dr,dc in directions: # To check 4 directions
                            curRow, curCol = dr + row, dc + col
                            # Check condition for validity
                            if curRow < 0 or curRow >= rows or curCol < 0 or curCol >= cols or grid[curRow][curCol] == 0:
                                continue
                            # Else, we've got an island
                            queue.append((curRow,curCol))
                            grid[curRow][curCol] = 0 # Mark before enqueue
                    # Once we've visited all the connected lands, count
                    visited = max(visited,cur_size)
        return visited
            

