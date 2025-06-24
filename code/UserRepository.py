# Компонент пользователи
import json

from code.model.User import User
from code.model.errors.UserNotFoundError import UserNotFoundError

class UserRepository:

    def __get_all_users(self):
        with open("database/users.json", encoding='UTF-8') as json_file:
            users = json.load(json_file)
            # Сохраняем логин и пароль каждого пользователя в сущность User
            return [User(**user) for user in users]

    def find_user(self, login, password):
        # Загружаем список пользователей из БД
        users = self.__get_all_users()
        for user in users:
            if user.username == login and user.password == password:
                # Если логин и пароль пользователя совпадает с тем что мы передали, то возвращаем id
                return user.id
        # Если пользователя не нашли, то выбрасываем ошибку
        raise UserNotFoundError
