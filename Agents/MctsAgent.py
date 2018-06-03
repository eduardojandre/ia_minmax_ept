import math
import time
import random
class Object(object):
    pass
class MctsAgent(object):
    def __init__(self, boardGame,ept,timeToPlay):
        self.boardGame=boardGame
        self.plays=0
        self.simuCounts=0
        self.ept=ept
        self.timeToPlay=timeToPlay
        self.root=None
    def uct(self,node):
        if(node.simulations==0):
            return float('inf')
        return (node.wins/node.simulations)+(4*math.sqrt(math.log(node.parent.simulations)/node.simulations))
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
    def backpropagation(self,node,result,win,lost,draw):
        while node.parent is not None:
            node=node.parent
            self.boardGame.popMove()
            node.simulations+=1
            if result==0:
                node.wins+=draw
            else:
                if result==1:
                    node.wins+=win
                else:
                    node.wins+=lost
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
        winValue=1
        lostValue=0
        drawValue=0.5
        if(not self.boardGame.gameIsOver()):
            improvement=(result-self.before)/self.before
            if(improvement>0.5):
                improvement=1
            if(improvement<-0.5):
                improvement=-1
            winValue=0.75 + improvement*0.2
            lostValue=0.25 + improvement*0.2
        if(result<0):
            result=-1
            if(self.boardGame.player != node.player):
                node.wins+=winValue
                result=1
            else:
                node.wins+=lostValue
        else:
            if(result>0):
                result=1
                if (self.boardGame.player == node.player):
                    node.wins+=winValue
                else:
                    node.wins+=lostValue
        node.simulations+=1
        if result==0:
            node.wins=drawValue
        else:
            result=result*-1
        for i in range(0,qtdMoves):
            self.boardGame.popMove()
        return result,winValue,lostValue,drawValue

    def play(self):
        self.plays+=1
        if self.root is None:
            self.root=self.createNode(None,None,self.boardGame.player)
        if(not self.root.expanded):
            self.expand(self.root,self.boardGame.turn)
            self.root.simulations=1
        self.simuCounts=0
        count=0
        self.before=self.boardGame.evaluate()
        start=time.time()

        while((time.time()-start)<self.timeToPlay):
            selected=self.select(self.root)
            result,win,lost,draw=self.simulate(selected)
            self.backpropagation(selected,result,win,draw,lost)
            count=count+1            
        best=float('-inf')
        print("MCTS Play")
        print("Nodes:")
        print(count)
        print("PlayOuts:")
        print(self.simuCounts)
        bestNode=None
        for child in self.root.childs:
            if(child.wins>best):
                best=child.wins
                bestNode=child
        self.root=bestNode
        self.boardGame.pushMove(bestNode.move)
        return bestNode.move
    def pushOponnentMove(self,move):
        self.boardGame.pushMove(move)
        newRoot=None
        if self.root is not None:
            for child in self.root.childs:
                if child.move==move:
                    newRoot=child
                    newRoot.parent=None
                    newRoot.player=self.boardGame.player
                    break
        self.root=newRoot
    def printStats(self):
        print("--------------Stats--------------")
        print("Plays: " + str(self.plays))
        print("---------------MCts--------------")
    def getStats(self):
        return str(self.plays )