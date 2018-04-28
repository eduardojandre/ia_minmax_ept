from TicTacToe import TicTacToe
from AlphaBetaAgent import AlphaBetaAgent
import random
tictac=TicTacToe()
agent=AlphaBetaAgent(tictac)

turn='x'
opponent='o'

board=tictac.createBoard()
board[0]=['o','o',None]
board[2]=['x',None,'x']
playing=True
#umanTurn=bool(int(input("Human starts? ")))#
humanTurn=0
tictac.printBoard(board)
while playing:
    if humanTurn:
        tictac.humanPlay(board,turn)
        humanTurn=False
    else:
        v,board=agent.alphabeta(board,10000000,float('-inf'),float('inf'),True,turn,opponent)
        #board=random.choice(boards)
        humanTurn=True
    if tictac.gameIsOver(board,turn):
        playing=False
    tmp=turn
    turn=opponent
    opponent=tmp
    tictac.printBoard(board)
