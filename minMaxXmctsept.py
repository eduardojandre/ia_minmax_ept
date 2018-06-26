import Engine.chessmain as eng
from Boards.ChessGame import ChessGame
from Agents.AlphaBetaAgent import AlphaBetaAgent
from Agents.MctsAgent import MctsAgent



result=[]
for i in range(0,20):
    chess=ChessGame(True)
    chess2=ChessGame(False)
    alpha=AlphaBetaAgent(chess,3)
    mcts=MctsAgent(chess2,4,20,False)
    
    result.append(eng.play(alpha,mcts))
print(result)