# Define some colors
from game.Cell import Cell

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (211, 211, 211)

def getCellColor(cell: Cell):
    if cell.isFlipped and not cell.isMine:
        color = GRAY
    elif cell.isFlipped and cell.isMine:
        color = RED
    elif cell.isFlagged:
        color = YELLOW
    else:
        color = WHITE

    return color