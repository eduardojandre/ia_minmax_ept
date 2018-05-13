import time

class AlphaBetaAgent(object):
    def __init__(self, boardGame):
        self.boardGame=boardGame
    def play(self,depth):
        start=time.time()
        v,move=self.alphabeta(depth,float('-inf'),float('inf'),True)
        self.boardGame.pushMove(move)
        print("AlphaBetaAgent")
        print("Time: ")
        print(time.time()-start)
        return move
    def alphabeta(self, depth, a, b, maximizingPlayer):
        game=self.boardGame
        if (depth == 0 or game.gameIsOver()): #limit of search or node is a terminal node
            val=game.evaluate(),game.getLastMove() #the heuristic value of node
            return val
        moves=game.availableMoves()
        if (maximizingPlayer):
            vBest=float('-inf')
            bestChild=None
            for child in moves:
                game.pushMove(child)
                v,move =self.alphabeta(depth - 1, a, b, False)
                game.popMove()
                if(v>=vBest):
                    vBest=v
                    bestChild=child
                a = max(a, vBest)
                if (b <= a):
                    vBest=float('inf')
                    break #(* β cut-off *)
            return vBest,bestChild
        else:
            vBest = float('inf')
            bestChild=None
            for child in moves:
                game.pushMove(child)
                v,move = self.alphabeta(depth - 1, a, b, True)
                game.popMove()
                if(v<=vBest):
                    vBest=v
                    bestChild=child
                b = min(b, vBest)
                if (b <= a):
                    vBest=float('-inf')
                    break #(* α cut-off *)
            return vBest,bestChild