from random import randint

from game import BoardState
from game.Cell import Cell
from typing import Dict
from game.Coordinate import Coordinate
from game.GameExceptions import InvalidBoardException
from game.BoardState import BoardState


class Board:
    def __init__(self, sizeCoord: Coordinate, numMines: int):
        self.sizeCoord = Coordinate(sizeCoord.x, sizeCoord.y)

        self.numMines = numMines
        validateBoard(sizeCoord, numMines)

        self.board: Dict[Coordinate, Cell] = {}

    def getCell(self, coord: Coordinate) -> Cell:
        if coord not in self.board:
            raise InvalidBoardException("The cell requested is not part of the board")

        return self.board[coord]

    def initBoard(self):
        self.board = {}
        self.initCells()
        self.setCellVals()

    def initCells(self):
        mineLocations = self.getNewMineLocations()

        for y in range(self.sizeCoord.y):
            for x in range(self.sizeCoord.x):
                coord = Coordinate(x, y)
                cell = Cell()
                cell.isMine = coord.isInList(mineLocations)
                self.board[coord] = cell

    def getNewMineLocations(self):
        mineLocations = []

        while len(mineLocations) < self.numMines:
            randomX = randint(0, self.sizeCoord.x - 1)
            randomY = randint(0, self.sizeCoord.y - 1)
            newCoord = Coordinate(randomX, randomY)

            if not newCoord.isInList(mineLocations):
                mineLocations.append(newCoord)

        return mineLocations

    def setCellVals(self):
        for coord, cell in self.board.items():
            if cell.isMine:
                cellVal = BoardState.MINE
            else:
                cellVal = self.getNumAdjacentMines(coord)

            cell.setVal(cellVal)

    def getNumAdjacentMines(self, coord):
        adjacentCells = self.getAdjacentCells(coord)
        numAdjacentMines = len(list(filter(lambda cell: cell.isMine, adjacentCells)))

        return numAdjacentMines

    def getAdjacentCells(self, coord: Coordinate):
        return [self.board[c] for c in coord.getAdjacentCoordinates(self.sizeCoord)]

    def getMatrix(self):
        matrix = []
        for y in range(self.sizeCoord.y):
            row = []
            for x in range(self.sizeCoord.x):
                row.append(self.board[Coordinate(x, y)])
            matrix.append(row)

        return matrix

    def getGameGrid(self):
        return self.board

    def printBoard(self):
        for row in self.getMatrix():
            print(row)


def validateBoard(sizeCoord: Coordinate, numMines: int):
    if numMines > sizeCoord.x * sizeCoord.y:
        raise InvalidBoardException("More mines than tiles passed to a board")
