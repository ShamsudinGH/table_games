import AuthManager
from code.SessionManager import SessionManager
from code.model.errors.UserNotFoundError import UserNotFoundError
from AuthManager import AuthManager
from code.GamerRepository import GamerRepository

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

print("Игровое меню")

gamer_control = GamerRepository()
gamer_control.append_gamer("werf")