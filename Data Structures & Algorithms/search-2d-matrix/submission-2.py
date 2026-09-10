class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, btm = 0, len(matrix) - 1

        while top <= btm:
            mid = (top + btm) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                top = mid + 1
            else:
                btm = mid - 1
        
        if btm < 0:
            return False
        
        l, r = 0, len(matrix[btm]) - 1

        while l <= r:
            mid = (l + r) // 2
            if matrix[btm][mid] == target:
                return True
            elif matrix[btm][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False