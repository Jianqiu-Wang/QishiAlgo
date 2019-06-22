# Runtime: 480 ms, faster than 11.55% of Python3 online submissions for Shortest Bridge.
# Memory Usage: 15.8 MB, less than 54.51% of Python3 online submissions for Shortest Bridge.

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        self.n, self.m = len(A), len(A[0])
        self.visited = [[False for i in range(self.n)] for j in range(self.m)] 
        root_x, root_y = self.find_first_1(A) # find one node of first island
        self.island1 = [(root_x, root_y)]
        self.visited[root_x][root_y] = True
        self.find_first_island(root_x, root_y, A)
        self.find_neighbours(A) # find 0s around first island
        
        step = 1
        second_island_found = False
        while step > 0:
            temp_nodes = []
            for indice in self.queue2:
                x, y = indice[0], indice[1]
                for dx, dy in zip([0,0,1,-1],[1,-1,0,0]):
                    nx, ny = x+dx, y+dy
                    if self.in_bound(nx, ny) and (not self.visited[nx][ny]) and ((x+dx, y+dy) not in self.queue2):
                        if A[nx][ny]==0 :  
                            temp_nodes.append((nx, ny))
                            self.visited[nx][ny] = True
                        else:
                            second_island_found = True
                            break

            if second_island_found: 
                break
            else:
                self.queue2 = temp_nodes
                step = step + 1         
        return step
    
    def find_first_1(self, A):
        for i in range(self.n):
            for j in range(self.m):
                if A[i][j] == 1:
                    return (i,j)
    
    def find_first_island(self, x, y, A):
        for dx, dy in zip([0,0,1,-1],[1,-1,0,0]):
            if self.in_bound(x+dx, y+dy) and (not self.visited[x+dx][y+dy]) and (A[x+dx][y+dy] == 1):    
                self.island1.append((x+dx, y+dy))
                self.visited[x+dx][y+dy] = True
                self.find_first_island(x+dx, y+dy, A)
        
    def find_neighbours(self, A):
        self.queue2 = []  
        for indice in self.island1:
            x, y = indice[0], indice[1]
            for dx, dy in zip([0,0,1,-1],[1,-1,0,0]):
                if self.in_bound(x+dx, y+dy) and (not self.visited[x+dx][y+dy]) and ((x+dx, y+dy) not in self.island1) and (A[x+dx][y+dy]==0):    
                    self.queue2.append((x+dx, y+dy))
                    self.visited[x+dx][y+dy] = True
        
    def in_bound(self, x, y):
        if (x>=0 and x<=self.n-1) and (y>=0 and y<=self.m-1):
            return True
        else:
            return False