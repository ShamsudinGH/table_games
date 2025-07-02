class Game:
    """Сущность игры"""

    def __init__(self, id, game_name, game_price):
        self.id = id
        self.game_name = game_name
        self.game_price = game_price

    def __repr__(self):
        return f'Game(id={self.id}, name={self.game_name}, price={self.game_name})'

def create_common_game(new_id, game_name, game_price) -> Game:
    return Game(id=new_id, game_name=game_name, game_price=game_price)