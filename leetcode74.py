# Runtime: 28 ms, faster than 99.65% of Python3 online submissions for Search a 2D Matrix.
# Memory Usage: 13.7 MB, less than 98.66% of Python3 online submissions for Search a 2D Matrix.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """ Binary search idea:
        1. find largest row s.t. target > row[0]
        2. find if target in this row
        O(log(max(m,n)))
        """
        # find row index
        if len(matrix) == 0 or len(matrix[0]) == 0: return False
        column1 = [x[0] for x in matrix]
        start = 0
        end = len(column1) - 1
        while start < end - 1:
            mid = start + (end - start) // 2
            if column1[mid] > target:
                end = mid
            else:
                start = mid
        if column1[end] > target:
            row = start
        else:
            row = end    
        
        # find elment in row
        target_list = matrix[row]
        start = 0
        end = len(target_list) - 1
        while start < end - 1:
            mid = start + (end - start) // 2
            if target_list[mid] < target:
                start = mid
            else:
                end = mid
        
        if target_list[start] == target: return True
        if target_list[end] == target: return True
        return False
