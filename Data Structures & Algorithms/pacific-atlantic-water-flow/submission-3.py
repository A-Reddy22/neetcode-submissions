from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols=len(heights),len(heights[0])
        pq=deque()
        pv=set()
        #the fiver arguments are the current space, the future space both rows and colums, the q and the set

        def bfs(r,c,prevHeight,q,s):
            if r<0 or r>rows-1 or c<0 or c>cols-1 or heights[r][c]<prevHeight or (r,c) in s:
                return
            else:
                s.add((r,c))
                q.append([r,c])
        

        #everything in pacific
        for i in range(rows):
            pq.append([i,0])
            pv.add((i,0))
        for j in range(cols):
            pq.append([0,j])
            pv.add((0,j))
        

        #everything in atlantic 
        aq=deque()
        av=set()
        for i in range(rows):
            aq.append([i,cols-1])
            av.add((i,cols-1))
        for j in range(cols):
            aq.append([rows-1,j])
            av.add((rows-1,j))
        #pacific
        while pq:
            
            for i in range(len(pq)):
                i,j=pq.popleft()
                bfs(i+1,j,heights[i][j],pq,pv)
                bfs(i-1,j,heights[i][j],pq,pv)
                bfs(i,j+1,heights[i][j],pq,pv)
                bfs(i,j-1,heights[i][j],pq,pv)
        
        #atlantic
        while aq:
            
            for i in range(len(aq)):
                i,j=aq.popleft()
                bfs(i+1,j,heights[i][j],aq,av)
                bfs(i-1,j,heights[i][j],aq,av)
                bfs(i,j+1,heights[i][j],aq,av)
                bfs(i,j-1,heights[i][j],aq,av)
        return list(pv & av)
            
      


            
        
        



        
        