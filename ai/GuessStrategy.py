from game.Cell import Cell
from game.Coordinate import Coordinate
from game.Game import Game
from random import randint, choice
from typing import List
from typing import Dict



class GuessStrategy:

    def __init__(self):
        pass

    def getPlay(self, game: Game):
        x = randint(0, game.width - 1)
        y = randint(0, game.height - 1)

    def findLowestProbCell(self, game: Game) -> List[Coordinate]:
        #map of coordinate to num unflipped adjacent squares that aren't mines
        counts = self.getSafeAdjacentCounts(game)
        guesses = findMaxSafe(counts)

        guess = getRandomGuess(game) if len(guesses) == 0 else guesses[0]

    def getSafeAdjacentCounts(self, game: Game):
        safeAdjacentCounts = {}

        for y in range(game.height):
            for x in range(game.width):
                coord = Coordinate(x, y)

                if game.canGetCell(coord):
                    currCell = game.getCell(coord)
                else:
                    continue

                adjCells = game.board.getAdjacentCells(coord)
                numUnmarkedAdj = len(list(filter(lambda cell: not cell.isFlipped and not cell.isFlagged, adjCells)))

                numSafeAdjacent = numUnmarkedAdj - currCell.val

                safeAdjacentCounts[numSafeAdjacent] = [coord] if numSafeAdjacent not in safeAdjacentCounts else safeAdjacentCounts[numSafeAdjacent].append(coord)

        return safeAdjacentCounts


def findMaxSafe(safeAdjacent: Dict[int, List[Coordinate]]) -> List[Coordinate]:
    maxFound = max(safeAdjacent.keys())
    return safeAdjacent[maxFound]

def getRandomGuess(game: Game, guesses: List[Coordinate] = []) -> Coordinate:
    if len(guesses) > 0:
        guess = choice(guesses)
    else:
        x = randint(0, game.width - 1)
        y = randint(0, game.height - 1)
        guess = Coordinate(x, y)

    return guess
