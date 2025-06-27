# Last updated: 6/27/2025, 5:22:50 AM
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # We can use backtrackiing to recursively go through this
        # matrix, and if the current character is inside our string
        # then we can continue
        # else recurse
        # At each grid, check 4 directions and check recursively
        # Time complexity: O(m*n)
        # Space complexity: O(m*n)
        if not board:
            return False
        res = False
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        rows, cols = len(board), len(board[0])

        def backtrack(r,c,i):
            if i == len(word): # Char not found
                return True
            if r >= rows or r < 0 or c >= cols or c < 0 or word[i] != board[r][c]:
                return False
            
            tmp = board[r][c]
            board[r][c] = "#"
            
            for dr, dc in directions:
                if backtrack(r+dr, c+dc, i+1):
                    return True
            
            board[r][c] = tmp
            return False
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r,c,0):
                    return True
        return False
            