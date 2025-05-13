# Last updated: 5/12/2025, 11:45:55 PM
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Edge case: word length > board length
        # won't have to worry about floats, ints, special characters, etc
        # dfs approach to search sequential cells
        # if we reach index length of word, then True
        # else False
        # Recursive steps: Search top, left, right, bottom 
        # if current character is same as word's character at index
        # add to our cur string and continue else skip
        Result = False
        row,col = len(board), len(board[0])
        def dfs(r,c, index):
            if index == len(word):
                return True
            if r < 0 or r >= row or c < 0 or c >= col or board[r][c] != word[index]:
                return False
            
            tmp = board[r][c]
            board[r][c] = "#"
            res = dfs(r+1,c,index+1) or dfs(r-1, c, index+1) or dfs(r, c+1, index+1) or dfs(r,c-1, index+1)

            board[r][c] = tmp
            return res

        if len(word) > row*col:
            return False
        for r in range(row):
            for c in range(col):
                if dfs(r,c,0):
                    return True
        return False