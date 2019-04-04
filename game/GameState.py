from enum import Enum


class GameState(Enum):
    NOT_STARTED = 1
    PLAYING = 2
    WON = 3
    LOST = 4
