from ChessGame import ChessGame
from AlphaBetaAgent import AlphaBetaAgent
from MctsAgent import MctsAgent
import random

playing=True
#humanTurn=bool(int(input("Human starts? ")))#
whiteTurn=True
chess=ChessGame(True)
chess2=ChessGame(False)
agent=AlphaBetaAgent(chess)
agent2=MctsAgent(chess2,4,2)
qtdPlays=0

chess.printBoard()
while playing:
    if whiteTurn:
        move=agent.play(5)
        chess2.pushMove(move)
        whiteTurn=False
    else:
        move=agent2.play(5)
        chess.pushMove(move)
        whiteTurn=True
    chess.printBoard()
    qtdPlays=qtdPlays+1
    if chess.gameIsOver():
        print("Game Over")
        print("Result: ")
        print(chess.board.result(False))
        print("Plays:")
        print(qtdPlays)
        playing=False
    
