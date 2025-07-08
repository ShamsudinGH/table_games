class Gamer:
    """Сущность игрока"""

    def __init__(self, id: int, gamer_name, nickname):
        self.id = id
        self.gamer_name = gamer_name
        self.nickname = nickname

    def __repr__(self):
        return f'Gamer({self.id}, {self.gamer_name}, {self.nickname})'

def create_common_gamer(new_id, name) -> Gamer:
    return Gamer(id=new_id, gamer_name=name, nickname=name)
