class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        ans=0

        def dfs(i,j):
            
            if i<0 or i>rows-1 or j<0 or j>cols-1 or grid[i][j]!=1:
                return 0
            else:
                area=1

                grid[i][j]=0
                area+=dfs(i-1,j)
                area+=dfs(i+1,j)
                area+=dfs(i,j+1)
                area+=dfs(i,j-1)
            return area
            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:

                    
                    ans=max(ans,dfs(i,j))
        return ans
        