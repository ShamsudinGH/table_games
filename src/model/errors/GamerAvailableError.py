class GamerAvailableError(Exception):
    def __init__(self, gamer_name):
        message = f'Игрок {gamer_name} уже существует в базе.'
        super().__init__(message)