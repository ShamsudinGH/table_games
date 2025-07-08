# Компонент пользователи
from src.model.User import User, create_default_user, Role
from src.model.encoders.UserEncoder import UserEncoder
from src.model.errors.UserNotFoundError import UserNotFoundError
from src.utils.JsonHelper import JsonHelper
from src.utils.ListHelper import last_item


class UserRepository:
    json_helper = JsonHelper()

    def append_user(self, login, password):
        all_users = self.__get_all_users()
        last_user = last_item(all_users)
        new_user_data = create_default_user(last_user.id + 1, login, password)
        all_users.append(new_user_data)

        self.json_helper.update_json("database/users.json", all_users, UserEncoder)

    def find_user(self, login, password) -> int:
        # Загружаем список пользователей из БД
        users = self.__get_all_users()
        for user in users:
            if user.username == login and user.password == password:
                # Если логин и пароль пользователя совпадает с тем что мы передали, то возвращаем id
                return user.id
        # Если пользователя не нашли, то выбрасываем ошибку
        raise UserNotFoundError

    def ban_user(self, user_id: int) -> None:
        all_users = self.__get_all_users()
        for user in all_users:
            if user.id == user_id:
                user.ban = True
                self.json_helper.update_json("database/users.json", all_users, UserEncoder)
                return None
        raise UserNotFoundError

    def is_role_admin(self, user_id: int) -> bool:
        role = self.__get_role__(user_id)
        return role == Role.ROLE_ADMIN

    def __get_all_users(self) -> list[User]:
        return self.json_helper.read_list_from_json("database/users.json", User)

    def __get_role__(self, user_id: int) -> Role:
        all_users = self.__get_all_users()
        for user in all_users:
            if user.id == user_id:
                return user.role
        raise UserNotFoundError