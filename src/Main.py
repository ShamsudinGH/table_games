from src.components.AuthManager import AuthManager
from src.components.SessionManager import SessionManager
from src.components.UserRepository import UserRepository
from src.model.errors.UserBannedError import UserBannedError
from src.model.errors.UserNotFoundError import UserNotFoundError
from src.panels.AuthorizationState import AuthorizationState
from src.panels.admin.AdminPanel import AdminPanel
from src.panels.state_machine.StateMachine import StateMachine
from src.panels.user.UserPanel import UserPanel

# Создаем экземпляр класса Компонент Авторизации
# auth_manager = AuthManager()
# # Создаем экземпляр класса Компонент Сессии
# session_manager = SessionManager()
# # Создаем экземпляр класса Компонент Пользователь
# user_repository = UserRepository()
#
# while True:
#     # Запрашиваем логин и пароль
#     login = input("Login: ")
#     password = input("Password: ")
#
#     # Создаем пустую переменную чтобы в нее записать id найденного пользователя
#     user_id = None
#     try:
#         # Попытка авторизоваться с помощью логина и пароля
#         user_id = auth_manager.authorize(login, password)
#     except UserNotFoundError:
#         print("Неверный логин или пароль")
#     except UserBannedError:
#         print("Пользователь забанен")
#     except:
#         print("Неизвестная ошибка при авторизации")
#
#     if user_id is not None:
#         # Если пользователь был найден, то сохраняем его id в Компонент Сессии
#         session_manager.set_user(user_id)
#         break
#
# user_id = session_manager.get_user()
# if user_repository.is_role_admin(user_id):
#     AdminPanel().run()
# else:
#     UserPanel().run()


state_machine = StateMachine(initial_state=AuthorizationState(),
                             source_destination_map=AuthorizationState.source_destination_map)
while True:
    print("-" * 45)
    new_state = state_machine.run_current_state()
    state_machine.change_state(new_state)

# user_repository = UserRepository()
# gamer_controller = GamerRepository()
#
# new_username = "sasha1111111"
# # gamer_controller.append_gamer(new_username)
# user_repository.append_user(new_username, new_username)
#
# print("Search...")
# # sasha_data = gamer_controller.search_gamer_by_name(new_username)
# # print(sasha_data)
# sasha_user_id = user_repository.find_user(new_username, new_username)
# print("user_id =", sasha_user_id)
#
# print(user_repository.is_role_admin(sasha_user_id))
#
#
# # print("Ban...")
# # user_repository.ban_user(sasha_user_id)
# # print(gamer_controller.search_gamer_by_name(new_username))
