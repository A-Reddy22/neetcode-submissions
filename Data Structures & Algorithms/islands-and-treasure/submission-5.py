from collections import deque
class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # use bfs to find distance
        # find distance from the gates themselves
        visited=set()
        rows,cols=len(grid),len(grid[0])
        q=deque()

        def check(r,c):
            if (r<0 or r>rows-1 or c<0 or c>cols-1 or grid[r][c]==-1 or (r,c) in visited):
                return
            visited.add((r,c))
            q.append([r,c])



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

                check(r+1,c)
                check(r-1,c)
                check(r,c+1)
                check(r,c-1)
            distance+=1

            


        
        