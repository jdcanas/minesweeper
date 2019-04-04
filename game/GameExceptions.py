class GameException(Exception):
    """Base class for other exceptions"""
    pass


class InvalidBoardException(GameException):
    pass
