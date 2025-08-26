import json

from src import ADMIN_MAP_JSON, USER_MAP_JSON
from src.components.AuthManager import AuthManager
from src.components.SessionManager import SessionManager
from src.components.UserRepository import UserRepository
from src.model.errors.UserBannedError import UserBannedError
from src.model.errors.UserNotFoundError import UserNotFoundError
from src.panels.Exit import Exit
from src.panels.admin.states.AdminInitial import AdminInitial
from src.panels.user.states.UserInitial import Initial as UserInitial, Initial
from src.panels.state_machine.State import State
from src.utils.JsonHelper import JsonHelper


class AuthorizationState(State):
    json_helper = JsonHelper()
    auth_manager = AuthManager()
    session_manager = SessionManager()
    user_repository = UserRepository()
    with open(ADMIN_MAP_JSON, "r", encoding='UTF-8') as admin_map_file:
        source_destination_map = json.load(admin_map_file)
    with open(USER_MAP_JSON, "r", encoding='UTF-8') as user_map_file:
        user_map = json.load(user_map_file)
    source_destination_map.update(user_map)



    def get_name(self):
        return "AuthorizationState"

    def run(self):
        print("[1] Войти")
        print("[0] Выйти")
        action = input("Выберите действие: ")
        if action == "1":
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
        elif action == "0":
            return Exit()

        user_id = self.session_manager.get_user()
        if self.user_repository.is_role_admin(user_id):
            return AdminInitial()
        else:
            return UserInitial()
