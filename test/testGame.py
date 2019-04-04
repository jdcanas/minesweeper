import unittest

from game.Board import Board
from game.Coordinate import Coordinate
from game.GameExceptions import InvalidBoardException


class TestBoard(unittest.TestCase):

    def setUp(self):
        pass

    def test_AdjacentCoordinatesCorner(self):
        sizeCoord = Coordinate(2, 2)

        cornerCoordinate1 = Coordinate(0, 0)
        cornerCoordinate2 = Coordinate(2, 2)
        cornerCoordinate3 = Coordinate(0, 2)
        cornerCoordinate4 = Coordinate(2, 0)

        self.assertEqual(3, len(cornerCoordinate1.getAdjacentCoordinates(sizeCoord)))

        self.assertTrue(any([coord.x == 1 and coord.y == 0 for coord in cornerCoordinate1.getAdjacentCoordinates(sizeCoord)]))
        self.assertTrue(any([coord.x == 0 and coord.y == 1 for coord in cornerCoordinate1.getAdjacentCoordinates(sizeCoord)]))
        self.assertTrue(any([coord.x == 1 and coord.y == 1 for coord in cornerCoordinate1.getAdjacentCoordinates(sizeCoord)]))

        self.assertEqual(3, len(cornerCoordinate2.getAdjacentCoordinates(sizeCoord)))
        self.assertEqual(3, len(cornerCoordinate3.getAdjacentCoordinates(sizeCoord)))
        self.assertEqual(3, len(cornerCoordinate4.getAdjacentCoordinates(sizeCoord)))

    def test_AdjacentCoordinatesMiddle(self):
        sizeCoord = Coordinate(3, 3)

        middleCoordinate = Coordinate(1, 1)

        self.assertEqual(8, len(middleCoordinate.getAdjacentCoordinates(sizeCoord)))

    def test_AdjacentCellMiddle(self):
        sizeCoord = Coordinate(3, 3)
        middleCoordinate = Coordinate(1, 1)

        board = Board(sizeCoord, 0)

        self.assertEqual(8, len(board.getAdjacentCells(middleCoordinate)))

    def test_AdjacentCoordinatesEdge(self):
        sizeCoord = Coordinate(3, 3)

        middleCoordinate = Coordinate(0, 1)

        self.assertEqual(5, len(middleCoordinate.getAdjacentCoordinates(sizeCoord)))

    def test_cellInit(self):
        sizeCoord = Coordinate(3, 3)
        numMines = 3
        boardObj = Board(sizeCoord, numMines)

        self.assertEqual(0, len(boardObj.board.keys()))

        boardObj.initCells()

        self.assertEqual(9, len(boardObj.board.keys()))
        self.assertEqual(3, len(list(filter(lambda cell: cell.isMine, boardObj.board.values()))))

    def test_mineInit(self):
        sizeCoord = Coordinate(3, 3)
        numMines = 4
        boardObj = Board(sizeCoord, numMines)

        self.assertEqual(numMines, len(boardObj.getNewMineLocations()))

    def testInvalidBoard(self):
        sizeCoord = Coordinate(3, 3)
        self.assertRaises(InvalidBoardException, Board, sizeCoord, 10)

if __name__ == '__main__':
    unittest.main()