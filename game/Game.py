from game.Board import Board
from game.Cell import Cell
from game.Coordinate import Coordinate
from game.GameExceptions import GameException
from game.GameState import GameState

class Game:

    numMines = 99
    width = 25
    height = 25

    def __init__(self):
        self.board = Board(Coordinate(self.width, self.height), self.numMines)
        self.state: GameState = GameState.NOT_STARTED

    def startGame(self):
        self.state = GameState.PLAYING
        self.board.initBoard()
        self.board.printBoard()

    def getGameGrid(self):
        return self.board.getGameGrid()

    def clickSquare(self, coord: Coordinate) -> GameState:
        if not self.state == GameState.PLAYING:
            return

        cell: Cell = self.board.getCell(coord)

        if cell.isFlagged: #do nothing
            return self.state

        if cell.isMine:
            cell.isFlipped = True
            self.state = GameState.LOST
            return self.state

        self.flipCell(cell)

        if self.isWin():
            self.state = GameState.WON

        return self.state

    def flagSquare(self, coord: Coordinate) -> GameState:
        self.board.getCell(coord).isFlagged = not self.board.getCell(coord).isFlagged

        if self.isWin():
            self.state = GameState.WON

        return self.state

    def isWin(self):

        for x in range(self.width):
            for y in range(self.height):
                cell = self.board.getCell(Coordinate(x, y))

                if cell.isMine and not cell.isFlagged: #all mines must be flagged
                    return False

                if not cell.isMine and not cell.isFlipped: #all non-mines must be flipped
                    return False
        return True

    def flipCell(self, cell: Cell):
        if not cell.isFlipped:
            cell.isFlipped = True

            if cell.val == 0:
                self.flipAdjacentCells(cell)
        else:
            if self.board.getNumAdjacentFlags(cell.coord) >= self.cell.val:
                self.flipAdjacentCells(cell)

    def adjacentToFlipBFS(self, root: Cell):
        toSearch = [root]
        found = [root]

        while len(toSearch) > 0:
            currNode = toSearch.pop()

            #mark all nodes adjacent as to be flipped
            found.extend(self.board.getAdjacentCells(currNode))

            #search all adj nodes with val = 0
            toSearch.extend(list(filter(lambda adjNode: (not adjNode.isFlagged and not adjNode.isFlipped and adjNode.val == 0 and adjNode not in toSearch and adjNode not in found), self.board.getAdjacentCells(currNode))))

    def flipAdjacentCells(self, cell: Cell):
        for adjCell in self.board.getAdjacentCells(cell.coord):
            if not adjCell.isFlagged and not adjCell.isFlipped and not adjCell.isMine:
                self.flipCell(adjCell)


