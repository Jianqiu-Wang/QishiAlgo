# Runtime: 744 ms, faster than 42.68% of Python online submissions for 01 Matrix.
# Memory Usage: 16.3 MB, less than 10.20% of Python online submissions for 01 Matrix.
from collections import deque
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        curr_level = []
        next_level = deque([])
        visited = [[False for i in range(n)] for j in range(m)]
        updated_matrix = [row[:] for row in matrix]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    curr_level.append((i,j))
                    visited[i][j] = True
        
        queue = deque(curr_level) 
        distance = 1
        while queue:
            (x, y) = queue.popleft()
            for dx, dy in zip([-1,1,0,0], [0,0,-1,1]):
                nx, ny = x+dx, y+dy
                if 0<=nx<=m-1 and 0<=ny<=n-1 and not visited[nx][ny]:
                    next_level.append((nx, ny))
                    visited[nx][ny] = True
                    updated_matrix[nx][ny] = distance
            if not queue:
                queue, next_level = next_level, deque([])
                distance = distance + 1
        return updated_matrix  