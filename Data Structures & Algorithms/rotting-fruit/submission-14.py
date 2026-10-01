from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        visited=set()
        q=deque()
        self.count=0

        def bfs(r,c):
            if r<0 or r>rows-1 or c<0 or c>cols-1 or (r,c) in visited or grid[r][c]==0:
                return
            if grid[r][c]==1:
                grid[r][c]=2
                self.count-=1
            visited.add((r,c))
            q.append([r,c])



        
       
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    q.append([i,j])
                    visited.add((i,j))
                elif grid[i][j]==1:
                    self.count+=1
        
        self.ans=0
        
        if self.count==0:
            return 0
        if not q:
            return -1
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                

                #bfs
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c-1)
                bfs(r,c+1)
            self.ans+=1
            if self.count ==0:
                return self.ans
        return -1
            
        
            

