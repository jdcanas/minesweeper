from game.Coordinate import Coordinate


class Cell:

    def __init__(self):
        self.isMine = False
        self.isFlipped = False
        self.isFlagged = False
        self.val = 0

    def setVal(self, val):
        self.val = val


    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self)



