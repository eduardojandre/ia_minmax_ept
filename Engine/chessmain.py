from Boards.ChessGame import ChessGame
from Agents.AlphaBetaAgent import AlphaBetaAgent
from Agents.MctsAgent import MctsAgent
import random


def play(whiteAgent,blackAgent):
    result=[]
    playing=True
    #humanTurn=bool(int(input("Human starts? ")))#
    whiteTurn=True
    chessWhite=whiteAgent.boardGame
    chessBlack=blackAgent.boardGame
    qtdPlays=0

    chessWhite.printBoard()
    while playing:
        if whiteTurn:
            move=whiteAgent.play()
            blackAgent.pushOponnentMove(move)
            whiteTurn=False
        else:
            move=blackAgent.play()
            whiteAgent.pushOponnentMove(move)
            whiteTurn=True
        chessWhite.printBoard()
        qtdPlays=qtdPlays+1
        if chessWhite.gameIsOver():
            print("Game Over")
            print("Result: ")
            tmp=chessWhite.board.result(False)
            print(tmp)
            result.append(tmp)
            result.append(whiteAgent.getStats())
            result.append(blackAgent.getStats())
            print("Plays:")
            print(qtdPlays)
            playing=False
            return result
    
