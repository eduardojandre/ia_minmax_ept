import chess
from IBoardGame import IBoardGame


class ChessGame(IBoardGame): 
    def __init__(self,machineStarts):
        self.board = chess.Board()
        if(machineStarts):
            self.player=chess.WHITE
            self.opponent=chess.BLACK
            self.turn=chess.WHITE
        else:
            self.turn=chess.BLACK
            self.player=chess.BLACK
            self.opponent=chess.WHITE
    def gameIsOver(self):
        return self.board.is_game_over(True)

    def valueForColor(self,color):
        resp=0
        resp+=len(self.board.pieces(chess.KNIGHT,color)) * 5
        resp+=len(self.board.pieces(chess.PAWN,color)) * 1
        resp+=len(self.board.pieces(chess.QUEEN,color)) * 10
        resp+=len(self.board.pieces(chess.BISHOP,color)) * 7
        resp+=len(self.board.pieces(chess.ROOK,color)) * 7
        return resp
    def evaluate(self):
        if(not self.board.is_game_over()):
            return self.valueForColor(self.player)-self.valueForColor(not self.player)
        else:
            result=self.board.result(True)
            resp=0
            if(len(result)>3):
                resp= 0
            else:
                if(result[0]=="1" and self.player==chess.WHITE):
                    resp=1
                else:
                    resp=-1
                resp=resp*1000000
                resp=resp-self.board.fullmove_number
        return resp
    def availableMoves(self):
        return list(self.board.legal_moves)
    def setBoard(self,board):
        self.board = board
    def printBoard(self):
        print("")
        print(self.board)
        print("")
        print("Fen: " + self.board.fen())
    def getBoard(self):
        return self.board
    def pushMove(self,move):
        self.board.push(move)
        self.changeTurn()
    def changeTurn(self):
        self.turn=not self.turn 
        self.opponent=not self.opponent
    def popMove(self):
        self.board.pop()
        self.changeTurn()
    def getLastMove(self):
        return self.board.peek()
    def humanPlay(self):
        valid=False
        while(not valid):
            try:
                inpu=input("Please enter your play: ")
                move=chess.Move.from_uci(inpu)
                valid=self.board.legal_moves.__contains__(move)
            except:
                print("Error")
            if(not valid):
                print("Invalid move")
                print(self.board.legal_moves)
            
        self.board.push(move)
        