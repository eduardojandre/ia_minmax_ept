class AlphaBetaAgent(object):
    def __init__(self, boardGame):
        self.boardGame=boardGame
    def alphabeta(self,node, depth, a, b, maximizingPlayer,turn,opponent):
        game=self.boardGame
        if (depth == 0 or game.gameIsOver(node,turn)): #limit of search or node is a terminal node
            return game.evaluate(node,turn),node #the heuristic value of node
        if maximizingPlayer:
            moves=game.availableMoves(node,turn)
        else:
            moves=game.availableMoves(node,opponent)
        if (maximizingPlayer):
            vBest=float('-inf')
            bestChild=None
            for child in moves:
                v,board =self.alphabeta(child, depth - 1, a, b, False,turn,opponent)
                if(v>=vBest):
                    vBest=v
                    bestChild=child
                a = max(a, vBest)
                if (b < a):
                    break #(* β cut-off *)
            return vBest,bestChild
        else:
            vBest = float('inf')
            bestChild=None
            for child in moves:
                v,board = self.alphabeta(child, depth - 1, a, b, True,turn,opponent)
                if(v<=vBest):
                    vBest=v
                    bestChild=child
                b = min(b, vBest)
                if (b < a):
                    break #(* α cut-off *)
            return vBest,bestChild