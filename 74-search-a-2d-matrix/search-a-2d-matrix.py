class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Go through each row
        # if l <= target <= r, search this row
        # Else continue
        # return True if found, false else
        # Going through each row, so is that O(m)?
        l,r = 0, len(matrix[0]) - 1
        for row in matrix:
            if target <= row[r] and target >= row[l]:
                # search this row
                while l <= r:
                    mid = (l + r) // 2
                    if row[mid] == target:
                        return True
                    elif row[mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1               
            else:
                continue
        return False            