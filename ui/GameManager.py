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
import ui.colors as colors

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
MARGIN = 5


class GameManager:
    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Initialize game object
        self.game = Game()

        # Set the HEIGHT and WIDTH of the screen
        self.screen = pygame.display.set_mode(self.getWindowSize())

        # Set title of screen
        pygame.display.set_caption("Minesweeper")

    def startGameLoop(self):
        self.game.startGame()

        # This tracks whether the user has closed the window, NOT whether the game is done
        done = False

        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()

        # -------- Main Program Loop -----------
        # Loop until the user clicks the close button.
        while not done:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouseClicked(event)

            # Draw the grid
            # the draw grid method takes the game such that it can be called outside of a game loop if desired
            self.drawGrid(self.game)

            # Limit to 60 frames per second
            clock.tick(60)

        # Be IDLE friendly. If you forget this line, the program will 'hang' on exit.
        pygame.quit()

    def getWindowSize(self):
        x = self.game.width * (WIDTH + MARGIN) + MARGIN
        y = self.game.height * (HEIGHT + MARGIN) + MARGIN

        return [y, x]

    def mouseClicked(self, event):
        # User clicks the mouse. Get the position
        pos = pygame.mouse.get_pos()
        # Change the x/y screen coordinates to grid coordinates
        x = pos[0] // (WIDTH + MARGIN)
        y = pos[1] // (HEIGHT + MARGIN)

        clickedCoord = Coordinate(x, y)

        if event.button == 3:  # right click
            self.game.flagSquare(clickedCoord)
        else:
            self.game.clickSquare(clickedCoord)

    def drawGrid(self, game: Game):

        grid = game.getGameGrid()
        # Set the screen background
        self.screen.fill(colors.BLACK)

        for y in range(game.height):
            for x in range(game.width):
                coord = Coordinate(x, y)
                cell = grid[x][y]

                pygame.draw.rect(self.screen,
                                 colors.getCellColor(cell),
                                 [(MARGIN + WIDTH) * y + MARGIN,
                                  (MARGIN + HEIGHT) * x + MARGIN,
                                  WIDTH,
                                  HEIGHT])

                if cell.isFlipped and not cell.isMine:
                    self.drawNumber(coord, cell.val)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    def drawNumber(self, coord: Coordinate, num: int):
        drawnNum = pygame.font.Font(None, 20).render(str(num), False, colors.BLACK)
        numRect = drawnNum.get_rect()
        numRect.center = getScreenPositionFromCoord(coord)
        self.screen.blit(drawnNum, numRect)


def getScreenPositionFromCoord(coord: Coordinate) -> (int, int):
    x = coord.x * (WIDTH + MARGIN) + WIDTH/2 + MARGIN/2
    y = coord.y * (HEIGHT + MARGIN) + HEIGHT/2 + MARGIN/2
    return y, x
