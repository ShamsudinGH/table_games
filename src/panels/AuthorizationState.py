from src.components.AuthManager import AuthManager
from src.components.SessionManager import SessionManager
from src.components.UserRepository import UserRepository
from src.model.errors.UserBannedError import UserBannedError
from src.model.errors.UserNotFoundError import UserNotFoundError
from src.panels.admin.states.AdminInitial import AdminInitial
from src.panels.state_machine.State import State
from src.panels.user.states.UserInitial import Initial as UserInitial


class AuthorizationState(State):
    auth_manager = AuthManager()
    session_manager = SessionManager()
    user_repository = UserRepository()

    def get_name(self):
        return "AuthorizationState"

    def run(self):
        while True:
            # Запрашиваем логин и пароль
            login = input("Login: ")
            password = input("Password: ")

            # Создаем пустую переменную чтобы в нее записать id найденного пользователя
            user_id = None
            try:
                # Попытка авторизоваться с помощью логина и пароля
                user_id = self.auth_manager.authorize(login, password)
            except UserNotFoundError:
                print("Неверный логин или пароль")
            except UserBannedError:
                print("Пользователь забанен")
            except:
                print("Неизвестная ошибка при авторизации")

            if user_id is not None:
                # Если пользователь был найден, то сохраняем его id в Компонент Сессии
                self.session_manager.set_user(user_id)
                break

        user_id = self.session_manager.get_user()
        if self.user_repository.is_role_admin(user_id):
            return AdminInitial()
        else:
            return UserInitial()
