from IBoardGame import IBoardGame

class TicTacToe(IBoardGame): 
    def gameIsOver(self,board,turn):
        return self.evaluate(board,turn) !=None
    def evaluate(self,board,turn):
        qtdEmpty=0
        resp=None
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j] is None:
                    qtdEmpty=qtdEmpty+1
        winner=None
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j] is None:
                    qtdEmpty=qtdEmpty+1
            if board[i][0]==board[i][1] and board[i][1] == board[i][2] and board[i][0] is not None:
                winner=board[i][0]
            if board[0][i]==board[1][i] and board[1][i] == board[2][i] and board[0][i] is not None:
                winner=board[0][i]
        if winner is None:
            if board[0][0]==board[1][1] and board[1][1] == board[2][2] and board[0][0] is not None:
                winner=board[0][0]
            else:
                if board[0][2]==board[1][1] and board[1][1] == board[2][0] and board[0][2] is not None:
                    winner=board[0][2]
        if winner is None and qtdEmpty==0:
            resp=0
        else:
            if winner is not None:
                if qtdEmpty>0:
                    resp=qtdEmpty+1
                else:
                    resp=1
                if winner != turn:
                    resp=resp*-1
        return resp
    def availableMoves(self,board,turn):
        resp=[]
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j] is None:
                    tmp=self.createBoard()
                    tmp[0]=board[0].copy()
                    tmp[1]=board[1].copy()
                    tmp[2]=board[2].copy()
                    tmp[i][j]=turn
                    resp.append(tmp)
        return resp
    def createBoard(self):
        board=[[None]*3,[None]*3,[None]*3]    
        return board
    def printBoard(self,board):
        print("Inicio")
        print(board[0])
        print(board[1])
        print(board[2])
        print("FIM")
    def humanPlay(self,board:list,turn:str):
        inpu=input("Please enter your play: ")
        p=inpu.split(",")
        lin=int(p[0])
        col=int(p[1])
        board[lin][col]=turn