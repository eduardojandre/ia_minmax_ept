import Engine.chessmain as eng
from Boards.ChessGame import ChessGame
from Agents.AlphaBetaAgent import AlphaBetaAgent
from Agents.MctsAgent import MctsAgent



result=[]
for i in range(0,5):
    chess=ChessGame(True)
    chess2=ChessGame(False)
    alpha=AlphaBetaAgent(chess2,5)
   # mcts=MctsAgent(chess2,float('inf'),5)
    ept=MctsAgent(chess,4,120)
    result.append(eng.play(ept,alpha))
print(result)