import math
import time
import random
class Object(object):
    pass
class MctsAgent(object):
    def __init__(self, boardGame,ept,timeToPlay):
        self.boardGame=boardGame
        self.jogada=0
        self.simuCounts=0
        self.ept=ept
        self.timeToPlay=timeToPlay
    def uct(self,node):
        if(node.simulations==0):
            return float('inf')
        return (node.wins/node.simulations)+(3*math.sqrt(math.log(node.parent.simulations)/node.simulations))
    def createNode(self,node,move,player):
        child=Object()
        child.simulations=0
        child.wins=0
        child.parent=node
        child.move=move
        child.expanded=False
        child.player=player
        return child
    def expand(self,node,player):
        node.childs=[]
        availableMoves=self.boardGame.availableMoves()
        for move in availableMoves:
            child=self.createNode(node,move,player)
            node.childs.append(child)
        node.expanded=True
    def select(self,node):
        if(node.simulations==0):
            return node
        if(not node.expanded):
            self.expand(node,self.boardGame.turn)
            if len(node.childs)==0:
                return node
            else:
                self.boardGame.pushMove(node.childs[0].move)
                return node.childs[0]
        if len(node.childs)==0:
            return node
        best=float('-inf')
        bestNode=None
        for child in node.childs:
            tmp=self.uct(child)
            if(tmp>best):
                best=tmp
                bestNode=child
        if bestNode is None:
            print('none')
        self.boardGame.pushMove(bestNode.move)
        return self.select(bestNode)
    def backpropagation(self,node,result):
        while node.parent is not None:
            node=node.parent
            self.boardGame.popMove()
            node.simulations+=1
            if result==0:
                node.wins+=0.5
            else:
                if result==1:
                    node.wins+=result
                result=result*-1
            
    def simulate(self,node):
        result=0
        qtdMoves=0
        while (not self.boardGame.gameIsOver() and qtdMoves < self.ept):
            move=random.choice(self.boardGame.availableMoves())
            self.boardGame.pushMove(move)
            qtdMoves+=1
            self.simuCounts=self.simuCounts+1
        result=self.boardGame.evaluate()
        if(result<0):
            result=-1
            if(self.boardGame.player != node.player):
                node.wins+=1 
                result=1
        else:
            if(result>0):
                result=1
                if (self.boardGame.player == node.player):
                    node.wins+=1 
        node.simulations+=1
        if result==0:
            node.wins=0.5
        else:
            result=result*-1
        for i in range(0,qtdMoves):
            self.boardGame.popMove()
        return result

    def play(self,depth):
        self.root=self.createNode(None,None,self.boardGame.player)
        self.expand(self.root,self.boardGame.turn)
        self.jogada+=1
        self.root.simulations=1
        self.simuCounts=0
        count=0
        start=time.time()
        while((time.time()-start)<self.timeToPlay):
            selected=self.select(self.root)
            result=self.simulate(selected)
            self.backpropagation(selected,result)
            count=count+1            
        best=float('-inf')
        print("MCTS Play")
        print("Nodes:")
        print(count)
        print("Simulations:")
        print(self.simuCounts)
        bestNode=None
        for child in self.root.childs:
            if(child.simulations>best):
                best=child.simulations
                bestNode=child
        self.boardGame.pushMove(bestNode.move)
        return bestNode.move