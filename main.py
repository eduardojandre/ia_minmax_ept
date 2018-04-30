from TicTacToe import TicTacToe
from MctsAgent import MctsAgent
from AlphaBetaAgent import AlphaBetaAgent
import random

playing=True
humanTurn=bool(int(input("Human starts? ")))#
tictac=TicTacToe("x",humanTurn)
#agent=AlphaBetaAgent(tictac)
agent=MctsAgent(tictac)


tictac.printBoard()
while playing:
    if humanTurn:
        tictac.humanPlay()
        humanTurn=False
    else:
        agent.play(10000000)
        humanTurn=True
    if tictac.gameIsOver():
        playing=False
    tictac.printBoard()
