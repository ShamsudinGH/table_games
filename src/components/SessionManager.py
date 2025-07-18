# Компонент Сессии
from src.utils._SingletonWrapper import singleton


@singleton
class SessionManager:

    # Установка текущего пользователя
    def set_user(self, id) ->int:
        self.id = id

    # Получение текущего пользователя
    def get_user(self) -> int:
        return self.id