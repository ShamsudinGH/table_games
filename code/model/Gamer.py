class Gamer:
    def __init__(self, id: int, gamer_name, nickname, status):
        self.id = id
        self.gamer_name = gamer_name
        self.nickname = nickname
        self.status = status

    def __repr__(self):
        return f'Gamer({self.id}, {self.gamer_name}, {self.nickname}, {self.status})'