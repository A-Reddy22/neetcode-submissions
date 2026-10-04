from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols=len(grid),len(grid[0])
        visited=set()
        q=deque()
        self.k=0

        def bfs(r,c):
            if r>rows-1 or r<0 or c<0 or c>cols-1 or (r,c) in visited or grid[r][c]!=1:
                return
            else:
                grid[r][c]=2
                q.append([r,c])
                visited.add((r,c))
                self.k-=1
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    q.append([i,j])
                    visited.add((i,j))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    self.k+=1
        if self.k==0:
            return 0
        
        minutes=0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                #run bfs
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
            minutes+=1
            if self.k==0:
                return minutes
        return -1

