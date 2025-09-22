# Компонент Авторизации
from src.components.UserRepository import UserRepository
from src.model.errors.UserBannedError import UserBannedError


class AuthManager:
    # Создаем экземпляр класса Компонент Пользователи
    user_repository = UserRepository()
    user_id = None

    def authorize(self, login, password) -> int:
        # Запрашиваем пользователя по переданному логину и паролю
        self.user_id = self.user_repository.find_user(login, password)
        if self.user_repository.is_user_banned(self.user_id):
            raise UserBannedError
        return self.user_id