from TicTacToe import TicTacToe
from AlphaBetaAgent import AlphaBetaAgent
import random

playing=True
humanTurn=bool(int(input("Human starts? ")))#
tictac=TicTacToe("x",humanTurn)
agent=AlphaBetaAgent(tictac)
boa=tictac.getBoard()


tictac.printBoard()
while playing:
    if humanTurn:
        tictac.humanPlay()
        humanTurn=False
    else:
        v,board=agent.alphabeta(10000000,float('-inf'),float('inf'),True)
        tictac.pushMove(board)
        humanTurn=True
    if tictac.gameIsOver():
        playing=False
    tictac.printBoard()
