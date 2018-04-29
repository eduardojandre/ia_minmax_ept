from IBoardGame import IBoardGame

class TicTacToe(IBoardGame): 
    def __init__(self,startPlayer,humanStarts):
        self.board=self.createBoard()
        self.movestack=[]
        if(startPlayer=="x"):
            self.opponent="o"
        else:
            self.opponent='x'
        self.turn=startPlayer
        if(humanStarts):
            self.player=self.opponent
        else:
            self.player=self.turn
        
    def gameIsOver(self):
        return self.evaluate() !=None
    def evaluate(self):
        board=self.board
        qtdEmpty=0
        resp=None
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
                if winner != self.player:
                    resp=resp*-1
        return resp
    def availableMoves(self):
        turn=self.turn
        resp=[]
        for i in range(0,3):
            for j in range(0,3):
                if self.board[i][j] is None:
                    tmp=self.createBoard()
                    tmp[0]=self.board[0].copy()
                    tmp[1]=self.board[1].copy()
                    tmp[2]=self.board[2].copy()
                    tmp[i][j]=turn
                    resp.append(tmp)
        return resp
    def createBoard(self):
        resp=[[None]*3,[None]*3,[None]*3]    
        return resp
    def setBoard(self,board):
        self.board=board
    def getBoard(self):
        return self.board
    def pushMove(self,move):
        self.movestack.insert(0,move)
        self.board=move
        self.changeTurn()
    def popMove(self):
        self.board=self.movestack.pop()
        self.changeTurn()
    def printBoard(self):
        print("Inicio")
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])
        print("FIM")
    def humanPlay(self):
        inpu=input("Please enter your play: ")
        p=inpu.split(",")
        lin=int(p[0])
        col=int(p[1])
        self.board[lin][col]=self.turn
        self.changeTurn()
    def getLastMove(self):
        return self.board
    def changeTurn(self):
        tmp=self.turn
        self.turn=self.opponent
        self.opponent=tmp
