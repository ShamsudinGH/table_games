# Компонент Авторизации
from src.components.UserRepository import UserRepository

class AuthManager:
    # Создаем экземпляр класса Компонент Пользователи
    user_repository = UserRepository()

    def authorize(self, login, password) -> int:
        # Запрашиваем пользователя по переданному логину и паролю
        user_id = self.user_repository.find_user(login, password)
        if self.user_repository.is_user_banned(user_id) is False:
            return user_id