# Пользователь
# TODO Добавить статус аккаунта (заблочен или нет)
class User:
    def __init__(self, id: int, username, password, gamer_id, ban: bool):
        self.id = id
        self.username = username
        self.password = password
        self.gamer_id = gamer_id
        self.ban = ban

    def __repr__(self):
        return f'User({self.id}, {self.username}, {self.password}, {self.gamer_id}, {self.ban})'