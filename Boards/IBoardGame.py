import abc

class IBoardGame(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def gameIsOver(self):
        raise NotImplementedError('users must define gameIsOver to use this base class')
    @abc.abstractmethod
    def evaluate(self):
        raise NotImplementedError('users must define evaluate to use this base class')
    @abc.abstractmethod
    def availableMoves(self):
        raise NotImplementedError('users must define availableMoves to use this base class')
    @abc.abstractmethod
    def setBoard(self,board):
        raise NotImplementedError('users must define setBoard to use this base class')
    @abc.abstractmethod
    def printBoard(self):
        raise NotImplementedError('users must define printBoard to use this base class')
    @abc.abstractmethod
    def getBoard(self):
        raise NotImplementedError('users must define getBoard to use this base class')
    @abc.abstractmethod
    def pushMove(self,move):
        raise NotImplementedError('users must define pushMove to use this base class')
    @abc.abstractmethod
    def popMove(self):
        raise NotImplementedError('users must define popMove to use this base class')
    @abc.abstractmethod
    def getLastMove(self):
        raise NotImplementedError('users must define getLastMove to use this base class')