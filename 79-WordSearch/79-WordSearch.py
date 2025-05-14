# Last updated: 5/13/2025, 11:26:40 PM
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # matrix traversal using dfs
        # if the current grid character is inside our word
        # then we will dfs from there after having marked it as visited
        # otherwise, skip
        # Time complexity O(m*n*4^n) where n is length of word
        # space complexity: O(m*n)
        rows,cols = len(board), len(board[0])
        def dfs(r,c,i):
            # base cases
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or word[i] != board[r][c]:
                return False
            # Visited and inside word
            tmp = board[r][c]
            board[r][c] = "#"
            # Now we'll have to search the four directions
            res = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r, c+1, i+1) or dfs(r,c-1,i+1)
            board[r][c] = tmp
            return res
        
        if len(word) > rows * cols:
            return False
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False