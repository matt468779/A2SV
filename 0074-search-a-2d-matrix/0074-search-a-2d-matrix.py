class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        hi = len(matrix)-1
        while lo <= hi:
            mid = (lo+hi)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                hi = mid - 1
            else:
                lo = mid + 1
                
        bound = hi
        lo = 0
        hi = len(matrix[0]) - 1
        while lo <= hi:
            mid = (lo+hi)//2
            if matrix[bound][mid] == target:
                return True
            elif matrix[bound][mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
                
        return False