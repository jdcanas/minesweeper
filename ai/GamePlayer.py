from game.Game import Game
from game.GameState import GameState
from ui.GameManager import GameManager


class GamePlayer:

    def __init__(self):
        self.game = Game()
        self.game.startGame()

    def play(self):
        currState = self.game.state

        while currState == GameState.PLAYING:
            self.game.clickSquare()

    def determineStrategy(self):


    def displayGame(self):
        manager = GameManager()
        manager.drawGrid(self.game)

