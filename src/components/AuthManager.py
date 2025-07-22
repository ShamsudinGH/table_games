# Компонент Авторизации
from src.components.UserRepository import UserRepository
from src.model.errors.UserBannedError import UserBannedError


class AuthManager:
    # Создаем экземпляр класса Компонент Пользователи
    user_repository = UserRepository()

    def authorize(self, login, password) -> int:
        # Запрашиваем пользователя по переданному логину и паролю
        user_id = self.user_repository.find_user(login, password)
        if self.user_repository.is_user_banned(user_id):
            raise UserBannedError
        return user_id