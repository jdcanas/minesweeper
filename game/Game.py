from game.Board import Board
from game.Cell import Cell
from game.Cell import filterFlagged
from game.Coordinate import Coordinate
from game.GameExceptions import GameException
from game.GameState import GameState

#TODO: make UIGame and AIGame

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

    def getCell(self, coord) -> Cell:
        if self.canGetCell(coord):
            return self.board[coord]
        else:
            raise GameException("Cannot get this cell, it is unflipped")

    def canGetCell(self, coord) -> bool:
        return self.board[coord].isFlipped

    def getGameGrid(self):
        return self.board.getGameGrid()

    def clickSquare(self, coord: Coordinate) -> GameState:
        if not self.state == GameState.PLAYING:
            return

        cell: Cell = self.board.getCell(coord)

        if cell.isFlagged: #do nothing
            return self.state

        self.flipCell(cell)

        self.state = self.computeState()
        return self.state

    def flagSquare(self, coord: Coordinate) -> GameState:
        self.board.getCell(coord).isFlagged = not self.board.getCell(coord).isFlagged

        return self.computeState()

    def computeState(self):
        state = GameState.PLAYING

        isInProgress = False
        isLost = False

        for x in range(self.width):
            for y in range(self.height):
                cell = self.board.getCell(Coordinate(x, y))

                if cell.isMine and cell.isFlipped:
                    isLost = True
                    break

                if cell.isMine and not cell.isFlagged:  # all mines must be flagged
                    isInProgress = True

                if not cell.isMine and not cell.isFlipped:  # all non-mines must be flipped
                    isInProgress = True

        if isLost:
            state = GameState.LOST
        elif isInProgress:
            state = GameState.PLAYING
        else:
            state = GameState.WON

        if state == GameState.WON: print("You won!")
        return state

    def flipCell(self, cell: Cell):
        toFlip = []
        if not cell.isFlipped:
            toFlip.append(cell)

            if cell.val == 0:
                toFlip = self.adjacentToFlipBFS(cell)
        else:
            if self.board.getNumAdjacentFlags(cell.coord) >= cell.val:
                toFlip = self.adjacentToFlipBFS(cell)

        for cell in toFlip:
            cell.isFlipped = True

    def adjacentToFlipBFS(self, root: Cell):
        toSearch = [root]
        found = [root]

        while len(toSearch) > 0:
            currNode = toSearch.pop()

            adjacentCells = self.board.getAdjacentCells(currNode.coord)

            #search all adj nodes with val = 0
            toSearch.extend(list(filter(lambda adjNode:
                                        (not adjNode.isFlagged
                                         and not adjNode.isFlipped
                                         and adjNode.val == 0
                                         and adjNode not in toSearch
                                         and adjNode not in found),
                                        self.board.getAdjacentCells(currNode.coord))))

            #mark all nodes adjacent as to be flipped
            found.extend(filterFlagged(adjacentCells))

        return found

    def flipAdjacentCells(self, cell: Cell):
        for adjCell in self.board.getAdjacentCells(cell.coord):
            if not adjCell.isFlagged and not adjCell.isFlipped and not adjCell.isMine:
                self.flipCell(adjCell)


