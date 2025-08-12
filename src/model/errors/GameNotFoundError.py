class GameNotFoundError(Exception):
    def __init__(self, *args):
        message = 'К сожалению, игра не найдена'
        super().__init__(message)