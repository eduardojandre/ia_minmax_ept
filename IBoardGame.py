import abc

class IBoardGame(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def gameIsOver(self,board,turn):
        raise NotImplementedError('users must define gameIsOver to use this base class')
    @abc.abstractmethod
    def evaluate(self,board,turn):
        raise NotImplementedError('users must define evaluate to use this base class')
    @abc.abstractmethod
    def availableMoves(self,board,turn):
        raise NotImplementedError('users must define availableMoves to use this base class')
    @abc.abstractmethod
    def createBoard(self):
        raise NotImplementedError('users must define availableMoves to use this base class')
    @abc.abstractmethod
    def printBoard(self,board):
        raise NotImplementedError('users must define availableMoves to use this base class')
    