class Coordinate:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def getAdjacentCoordinates(self, sizeCoord):
        adjacents = []
        directions = [-1, 0, 1]

        for x in directions:
            adjacentX = self.x + x

            if adjacentX < 0 or adjacentX > sizeCoord.x - 1:
                continue

            for y in directions:
                adjacentY = self.y + y

                if adjacentY < 0 or adjacentY > sizeCoord.y - 1:
                    continue

                if adjacentY == self.y and adjacentX == self.x:
                    continue

                adjacents.append(Coordinate(adjacentX, adjacentY))

        return adjacents

    def isInList(self, coordList):
        return any([self == loc for loc in coordList])

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __repr__(self):
        return str(self)





