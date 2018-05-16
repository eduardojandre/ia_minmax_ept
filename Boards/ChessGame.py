import chess
from Boards.IBoardGame import IBoardGame


class ChessGame(IBoardGame): 
    queens=[
        -20,-10,-10, -5, -5,-10,-10,-20,
        -10,  0,  5,  0,  0,  0,  0,-10,
        -10,  5,  5,  5,  5,  5,  0,-10,
          0,  0,  5,  5,  5,  5,  0, -5,
         -5,  0,  5,  5,  5,  5,  0, -5,
        -10,  0,  5,  5,  5,  5,  0,-10,
        -10,  0,  0,  0,  0,  0,  0,-10,
        -20,-10,-10, -5, -5,-10,-10,-20
    ]
    rock=[
          0,  0,  0,  5,  5,  0,  0,  0,
         -5,  0,  0,  0,  0,  0,  0, -5,
         -5,  0,  0,  0,  0,  0,  0, -5,
         -5,  0,  0,  0,  0,  0,  0, -5,
         -5,  0,  0,  0,  0,  0,  0, -5,
         -5,  0,  0,  0,  0,  0,  0, -5,
          5, 10, 10, 10, 10, 10, 10,  5,
          0,  0,  0,  0,  0,  0,  0,  0   
    ]
    bishop=[
        -20,-10,-10,-10,-10,-10,-10,-20,
        -10,  5,  0,  0,  0,  0,  5,-10,
        -10, 10, 10, 10, 10, 10, 10,-10,
        -10,  0, 10, 10, 10, 10,  0,-10,
        -10,  5,  5, 10, 10,  5,  5,-10,
        -10,  0,  5, 10, 10,  5,  0,-10,    
        -10,  0,  0,  0,  0,  0,  0,-10,
        -20,-10,-10,-10,-10,-10,-10,-20
    ]
    knight=[
        -50,-40,-30,-30,-30,-30,-40,-50,
        -40,-20,  0,  5,  5,  0,-20,-40,
        -30,  5, 10, 15, 15, 10,  5,-30,
        -30,  0, 15, 20, 20, 15,  0,-30,
        -30,  5, 15, 20, 20, 15,  5,-30,
        -30,  0, 10, 15, 15, 10,  0,-30,
        -40,-20,  0,  0,  0,  0,-20,-40,
        -50,-40,-30,-30,-30,-30,-40,-50
    ]
    pawn=[
        0,  0,  0,  0,  0,  0,  0,  0,
        5, 10, 10,-20,-20, 10, 10,  5,
        5, -5,-10,  0,  0,-10, -5,  5,
        0,  0,  0, 20, 20,  0,  0,  0,
        5,  5, 10, 25, 25, 10,  5,  5,
        10, 10, 20, 30, 30, 20, 10, 10,
        50, 50, 50, 50, 50, 50, 50, 50,
         0,  0,  0,  0,  0,  0,  0,  0 
    ]
    def __init__(self,machineStarts):
        self.board = chess.Board()
        self.turn=chess.WHITE
        if(machineStarts):
            self.player=chess.WHITE
            self.opponent=chess.BLACK
        else:
            self.player=chess.BLACK
            self.opponent=chess.WHITE
    def gameIsOver(self):
        return self.board.is_game_over(False)

    def valueForColor(self,color):
        resp=0
        pieceAd=0
        if(color==chess.BLACK):
            pieceAd=-63
        for piece in self.board.pieces(chess.QUEEN,color):
            resp=resp+900+self.queens[piece+pieceAd]
        for piece in self.board.pieces(chess.ROOK,color):
            resp=resp+500+self.rock[piece+pieceAd]
        for piece in self.board.pieces(chess.BISHOP,color):
            resp=resp+330+self.bishop[piece+pieceAd]
        for piece in self.board.pieces(chess.KNIGHT,color):
            resp=resp+320+self.knight[piece+pieceAd]
        for piece in self.board.pieces(chess.PAWN,color):
            resp=resp+100+self.pawn[piece+pieceAd]

        
        #resp+=len(self.board.pieces(chess.KNIGHT,color)) * 320
        #resp+=len(self.board.pieces(chess.PAWN,color)) * 100
        #resp+=len(self.board.pieces(chess.QUEEN,color)) * 900
        #resp+=len(self.board.pieces(chess.BISHOP,color)) * 330
        #resp+=len(self.board.pieces(chess.ROOK,color)) * 500
        return resp
    def evaluate(self):
        if(not self.board.is_game_over()):
            return self.valueForColor(self.player)-self.valueForColor(not self.player)-self.board.fullmove_number
        else:
            result=self.board.result(False)
            resp=0
            if(len(result)>3):
                resp= 0
            else:
                if(result[0]=="1" and self.player==chess.WHITE):
                    resp=1
                else:
                    resp=-1
                resp=resp*1000000000
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
        