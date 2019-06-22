# Runtime: 108 ms, faster than 20.75% of Python3 online submissions for Number of Islands.
# Memory Usage: 14.2 MB, less than 34.02% of Python3 online submissions for Number of Islands.
class Solution:
    res = 0
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == '1': 
                    self.res = self.res + 1
                    self.dfs(i,j)
        return self.res
    
    def dfs(self, i, j):
        if self.grid[i][j] == '0': 
            return
        else:
            self.grid[i][j] = '0' # override element
            for di, dj in zip([1,-1,0,0],[0,0,1,-1]):
                if 0<=i+di<self.m and 0<=j+dj<self.n: 
                    self.dfs(i+di, j+dj)