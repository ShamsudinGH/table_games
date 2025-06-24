# Пользователь
# TODO Добавить статус аккаунта (заблочен или нет)
class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return "User(" + self.id + ", " + self.username + ", " + self.password + ")"