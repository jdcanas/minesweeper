from game.Coordinate import Coordinate


class Cell:

    def __init__(self, coord):
        self.isMine = False
        self.isFlipped = False
        self.isFlagged = False
        self.val = 0
        self.coord = coord

    def setVal(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self)


def filterFlagged(cells):
    return list(filter(lambda cell: not cell.isFlagged, cells))



