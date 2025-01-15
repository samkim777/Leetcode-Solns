class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(logn) + O(logm) Time complexity
        # O(1) space
        ROW, COL = len(matrix), len(matrix[0])
        top, bot = 0, ROW - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]: # Bigger than biggest in that row
                top = row + 1
            elif target < matrix[row][0]: # smaller than smallest
                bot = row - 1
            else: # In this current row
                break

        # If we exit while loop above but no found, target no existe
        if not (top <= bot):
            return False
        # Now loop through our found row
        row = (top + bot) // 2
        l,r = 0, COL - 1
        while l <= r:
            mid = (l+r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False                                