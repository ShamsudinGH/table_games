from src.components.GameRepository import GameRepository
from src.components.SessionManager import SessionManager
from AuthManager import AuthManager

# Создаем экземпляр класса Компонент Авторизации
auth_manager = AuthManager()
# Создаем экземпляр класса Компонент Сессии
session_manager = SessionManager()

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
#     except:
#         print("Неизвестная ошибка при авторизации")
#
#     if user_id is not None:
#         # Если пользователь был найден, то сохраняем его id в Компонент Сессии
#         session_manager.set_user(user_id)
#         break

# print("Игровое меню")
# game_controller = GamerRepository()
# user_repository = UserRepository()
#
# new_username = "sasha1111111"
# game_controller.append_gamer(new_username)
# user_repository.append_user(new_username, new_username)
#
# print("Search...")
# sasha_data = game_controller.search_gamer_by_name(new_username)
# print(sasha_data)
# sasha_user_id = user_repository.find_user(new_username, new_username)
# print("user_id =", sasha_user_id)
#
# print("Ban...")
# user_repository.ban_user(sasha_user_id)
# print(game_controller.search_gamer_by_name(new_username))

print("Игровое меню")
game_controller = GameRepository()

new_gamename = "Manchkin"
game_controller.append_game(new_gamename, 100)

print("Search...")
game_data = game_controller.search_game(new_gamename)
print(game_data)

print("Delete...")
game_controller.delete_game(new_gamename)
