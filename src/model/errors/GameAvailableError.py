class GameAvailableError(Exception):
    def __init__(self, game_name):
        message = f'Игра {game_name} уже существует в базе.'
        super().__init__(message)