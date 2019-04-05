from game.Board import Board
from game.Coordinate import Coordinate

def main():
	sizeCoord = Coordinate(width, height)
	board = Board(sizeCoord, mines)

	board.initBoard()

	board.printBoard()


if __name__ == '__main__':
	main()
