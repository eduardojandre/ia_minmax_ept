from ChessGame import ChessGame
from AlphaBetaAgent import AlphaBetaAgent
from MctsAgent import MctsAgent
import random

playing=True
humanTurn=bool(int(input("Human starts? ")))#
chess=ChessGame(not humanTurn)
#agent=AlphaBetaAgent(chess)
agent=MctsAgent(chess)


chess.printBoard()
while playing:
    if humanTurn:
        chess.humanPlay()
        humanTurn=False
    else:
        agent.play(3)
        humanTurn=True
    if chess.gameIsOver():
        playing=False
    chess.printBoard()
