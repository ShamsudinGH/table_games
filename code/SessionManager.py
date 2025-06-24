# Компонент Сессии
from code.utils._SingletonWrapper import singleton


@singleton
class SessionManager:

    # Установка текущего пользователя
    def set_user(self, id):
        self.id = id

    # Получение текущего пользователя
    def get_user(self):
        return self.id