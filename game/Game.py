from game.Board import Board
from game.Cell import Cell
from game.Coordinate import Coordinate
from game.GameExceptions import GameException
from game.GameState import GameState

from typing import List

class Game:

    numMines = 5
    width = 3
    height = 3

    def __init__(self):
        self.board = Board(Coordinate(self.width, self.height), self.numMines)
        self.state: GameState = GameState.NOT_STARTED

    def startGame(self):
        self.state = GameState.PLAYING

    def getGameGrid(self):
        return self.board.getGameGrid()

    def clickSquare(self, coord: Coordinate) -> GameState:
        if not self.state == GameState.PLAYING:
            raise GameException("You cannot make a move when the game state is " + self.state)

        cell: Cell = self.board.getCell(coord)

        if cell.isFlagged: #do nothing
            return self.state

        if cell.isMine:
            self.state = GameState.LOST
            return self.state

        if not cell.isFlipped:
            cell.isFlipped = True

        if cell.isFlipped:
            #flip adjacent squares
            pass

        if self.isWin():
            self.state = GameState.WON

        return self.state


    def flagSquare(self, coord: Coordinate):
        self.board.getCell(coord).isFlagged = True

    def isWin(self) -> List[List[str]]:

        for x in range(self.width):
            for y in range(self.height):
                cell = self.board.getCell(Coordinate(x, y))

                if cell.isMine and not cell.isFlagged: #all mines must be flagged
                    return False

                if not cell.isMine and not cell.isFlipped: #all non-mines must be flipped
                    return False

        return True
