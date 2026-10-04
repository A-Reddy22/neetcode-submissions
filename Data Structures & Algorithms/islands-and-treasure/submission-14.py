from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # first have to get the rows and columns of the company
        #start at the 0's and find everything visitable and change that to the distance
        #run bfs
        q=deque()
        visited=set()
        rows,cols=len(grid),len(grid[0])
        def bfs(r,c):
            if r<0 or r>rows-1 or c<0 or c>cols-1 or grid[r][c]==-1 or (r,c) in visited:
                return
            else:
                q.append([r,c])
                visited.add((r,c))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    q.append([i,j])
                    visited.add((i,j))
        
        distance=0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=distance
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
            distance+=1

        
        