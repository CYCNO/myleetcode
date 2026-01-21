# My Solution Time COmplexity: O(MlogN)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            len_matrix = len(matrix[i])
            if matrix[i][len_matrix - 1] >= target:
                l, r = 0, len_matrix - 1
                
                while l<=r:
                    mid = (l+r)//2
                    val = matrix[i][mid]
                    if val > target:
                        r = mid - 1
                    elif val < target:
                        l = mid + 1
                    else:
                        return True
                        break
        return False

# More optimized and O(log(m*n))
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, (rows * cols) - 1
        
        while low <= high:
            mid = (low + high) // 2
            mid_val = matrix[mid // cols][mid % cols]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return False
