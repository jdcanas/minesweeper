"""
 Example program to show using an array to back a grid on-screen.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import pygame

from game.Cell import Cell
from game.Coordinate import Coordinate
from game.Game import Game

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (211, 211, 211)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
MARGIN = 5

# Initialize pygame
pygame.init()
game = Game()
game.startGame()


def getWindowSize():
    x = game.width * (WIDTH + MARGIN) + MARGIN
    y = game.height * (HEIGHT + MARGIN) + MARGIN

    return [y, x]

# Set the HEIGHT and WIDTH of the screen
screen = pygame.display.set_mode(getWindowSize())

def main():
    # Create a 2 dimensional array. A two dimensional
    # array is simply a list of lists.
    # grid = []
    # for row in range(10):
    #     # Add an empty array that will hold each cell
    #     # in this row
    #     grid.append([])
    #     for column in range(10):
    #         grid[row].append(0)  # Append a cell



    # Set title of screen
    pygame.display.set_caption("Minesweeper")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseClicked(event)
        # Draw the grid
        drawGrid()

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

def mouseClicked(event):
    # User clicks the mouse. Get the position
    pos = pygame.mouse.get_pos()
    # Change the x/y screen coordinates to grid coordinates
    x = pos[0] // (WIDTH + MARGIN)
    y = pos[1] // (HEIGHT + MARGIN)

    clickedCoord = Coordinate(x, y)

    if event.button == 3:  # right click
        game.flagSquare(clickedCoord)
    else:
        game.clickSquare(clickedCoord)

    print("Click ", pos, "Grid coordinates: ", x, y)

def drawGrid():
    # Set the screen background
    screen.fill(BLACK)

    grid = game.getGameGrid()

    for y in range(game.height):
        for x in range(game.width):
            coord = Coordinate(x, y)
            cell = grid[x][y]

            pygame.draw.rect(screen,
                             getCellColor(cell),
                             [(MARGIN + WIDTH) * y + MARGIN,
                              (MARGIN + HEIGHT) * x + MARGIN,
                              WIDTH,
                              HEIGHT])

            if cell.isFlipped and not cell.isMine:
                drawNumber(coord, cell.val)

def drawNumber(coord: Coordinate, num: int):
    drawnNum = pygame.font.Font(None, 20).render(str(num), False, BLACK)
    numRect = drawnNum.get_rect()
    numRect.center = getScreenPositionFromCoord(coord)
    screen.blit(drawnNum, numRect)


def getScreenPositionFromCoord(coord: Coordinate) -> (int, int):
    x = coord.x * (WIDTH + MARGIN) + WIDTH/2 + MARGIN/2
    y = coord.y * (HEIGHT + MARGIN) + HEIGHT/2 + MARGIN/2
    return y, x

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


if __name__ == '__main__':
    main()

