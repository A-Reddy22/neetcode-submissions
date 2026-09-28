class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # first i should get the length of rows and columns



        rows,col=len(grid), len(grid[0])

        number_of_islands=0

        def dfs(i,j):
            if i<0 or i>=rows or j<0 or j>=col or grid[i][j]!="1":
                return 
            else:
                grid[i][j]="0"
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)



        for i in range(rows):
            for j in range(col):
                if grid[i][j]=="1":
                    number_of_islands+=1
                    
                    dfs(i,j)
        return number_of_islands

        