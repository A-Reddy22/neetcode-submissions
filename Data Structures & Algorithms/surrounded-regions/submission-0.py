class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # find the O's that are on the border so what we do is we find 
        #find the Os on the border then do dfs on it so we can mark all of that and then continue
        # these 0's we can mark on the board as Ts and then move on 

        # find the 0 on the border

        def dfs(i,j):
            if i<0 or j<0 or i>rows-1 or j>cols-1 or board[i][j]!="O":
                return
            board[i][j]="T"
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        rows,cols=len(board),len(board[0])
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='O' and (i in ([0,rows-1]) or j in ([0,cols-1])):
                    dfs(i,j)

        # make all other O into X
        for i in range((rows)):
            for j in range(cols):
                if board[i][j]=="O":
                    board[i][j]="X"
        
        for i in range((rows)):
            for j in range(cols):
                if board[i][j]=="T":
                    board[i][j]="O"
        
        