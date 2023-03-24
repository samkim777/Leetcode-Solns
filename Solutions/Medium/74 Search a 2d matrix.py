class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Say target = 15
        # In the given matrix, 15 is greater than first integer
        # of 1st and 2nd row, but not 3rd
        # So, 15 must be inside 2nd row
        # We check if 15 in the mid point of row 2, then iterate
        if target > matrix[-1][-1] or target < matrix[0][0]: 
            # Target out of bounds
            return False
        ll,rl = 0, len(matrix) - 1
        mid = 0
        while (ll <= rl): # O(log n)
            mid = (ll + rl) // 2
            l,r = 0, len(matrix[mid]) - 1
            if target > matrix[mid][-1]: # Target greater than cur lis
                ll = mid + 1
            elif target < matrix[mid][0]: # Target smaller than cur list
                rl = mid - 1
            else:
                break # Found the list to search
        # Search the found list
        l,r = 0, len(matrix[mid]) - 1
        while (l <= r): # O(log m) 
            midpt = (l+r) // 2
            if target > matrix[mid][midpt]:
                l = midpt + 1
            elif target < matrix[mid][midpt]:
                r = midpt - 1
            else: 
                return True # Found number
        # Overall time complexity = O(log n) + O(log m) = O(log (m*n))        
 
        return False                
            