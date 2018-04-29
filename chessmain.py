from ChessGame import ChessGame
from AlphaBetaAgent import AlphaBetaAgent
import random

playing=True
humanTurn=bool(int(input("Human starts? ")))#
chess=ChessGame(not humanTurn)
agent=AlphaBetaAgent(chess)



chess.printBoard()
while playing:
    if humanTurn:
        chess.humanPlay()
        humanTurn=False
    else:
        v,move=agent.alphabeta(3,float('-inf'),float('inf'),True)
        chess.pushMove(move)
        humanTurn=True
    if chess.gameIsOver():
        playing=False
    chess.printBoard()
