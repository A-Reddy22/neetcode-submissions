from collections import deque 
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols=len(grid),len(grid[0])
        q=deque()

        def helper(r,c):
            if r<0 or r>rows-1 or c<0 or c>cols-1 or grid[r][c]==-1 or grid[r][c]!= 2147483647:
                return
            grid[r][c]=distance+1
            q.append([r,c])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    q.append([i,j])
        
        distance=0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=distance

                #bfs in four directions
                helper(r+1,c)
                helper(r,c-1)
                helper(r-1,c)
                helper(r,c+1)
            distance+=1


        