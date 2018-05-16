import Engine.chessmain as eng
from Boards.ChessGame import ChessGame
from Agents.AlphaBetaAgent import AlphaBetaAgent
from Agents.MctsAgent import MctsAgent



result=[]
for i in range(0,20):
    chess=ChessGame(True)
    chess2=ChessGame(False)
    alpha=AlphaBetaAgent(chess,5)
   # mcts=MctsAgent(chess2,float('inf'),120)
    mcts=MctsAgent(chess2,4,120)
    result.append(eng.play(alpha,mcts))
print(result)