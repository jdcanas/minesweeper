from game.Board import Board
from game.Coordinate import Coordinate

mines = 5
width = 3
height = 3


def main():
	sizeCoord = Coordinate(width, height)
	board = Board(sizeCoord, mines)

	board.initBoard()

	board.printBoard()


if __name__ == '__main__':
	main()
