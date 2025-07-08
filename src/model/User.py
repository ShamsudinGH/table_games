from enum import Enum

class Role(Enum):
    ROLE_USER = "role_user"
    ROLE_ADMIN = "role_admin"

class User:
    """Сущность пользователя"""

    def __init__(self, id: int, username, password, gamer_id, ban: bool, role: Role):
        self.id = id
        self.username = username
        self.password = password
        self.gamer_id = gamer_id
        self.ban = ban
        self.role = role

    def __repr__(self):
        return f'User({self.id}, {self.username}, {self.password}, {self.gamer_id}, {self.ban})'

def create_default_user(new_id, login, password) -> User:
    return User(id=new_id, username=login, password=password, gamer_id=new_id, ban=False, role=Role.ROLE_USER)