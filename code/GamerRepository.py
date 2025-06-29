import json

from code.model.Gamer import Gamer
from code.model.encoders.GamerEncoder import GamerEncoder
from code.model.encoders.UserEncoder import UserEncoder
from code.model.errors.UserNotFoundError import UserNotFoundError
from code.model.errors.GamerAvailableError import GamerAvailableError
from code.model.User import User
from code.UserRepository import UserRepository


class GamerRepository:

    def __get_all_gamers(self):
        with open("database/gamers.json", encoding='UTF-8') as json_file:
            gamers = json.load(json_file)
            return [Gamer(**gamer) for gamer in gamers]

    def __get_all_users(self):
        with open("database/users.json", encoding='UTF-8') as json_file:
            users = json.load(json_file)
            # Сохраняем логин и пароль каждого пользователя в сущность User
            return [User(**user) for user in users]

    def search_gamer_by_id(self, id):
        # Загружаем список игроков из БД
        gamers = self.__get_all_gamers()
        for gamer in gamers:
            if gamer.id == id:
                return gamer
        # Если игрока не нашли, то выбрасываем ошибку
        raise UserNotFoundError

    def search_gamer_by_name(self, user_name):
        # Загружаем список игроков из БД
        gamers = self.__get_all_gamers()
        for gamer in gamers:
            if gamer.gamer_name == user_name:
                # Если логин и пароль пользователя совпадает с тем что мы передали, то возвращаем id
                return gamer
        # Если пользователя не нашли, то выбрасываем ошибку
        raise UserNotFoundError

    def append_gamer(self, gamer_name):
        all_gamers = self.__get_all_gamers()
        all_users = self.__get_all_users()
        for gamer in all_gamers:
            if gamer.gamer_name == gamer_name:
                raise GamerAvailableError(gamer_name)
        last_gamer = all_gamers[-1]
        with open("database/gamers.json", "w", encoding='UTF-8') as json_file:
            new_gamer_data = Gamer(id=last_gamer.id+1, gamer_name=gamer_name, nickname=gamer_name, status="user")
            all_gamers.append(new_gamer_data)
            json.dump(all_gamers, json_file, indent=4, cls=GamerEncoder)
            with open("database/users.json", "w", encoding='UTF-8') as user_json_file:
                new_user_data = User(id=last_gamer.id+1, username=gamer_name, password=gamer_name,
                                     gamer_id=last_gamer.id+1, ban=False)
                all_users.append(new_user_data)
                json.dump(all_users, user_json_file, indent=4, cls=UserEncoder)

    def user_ban(self, user_id):
        all_users = self.__get_all_users()
        for user in all_users:
            if user.id == user_id:
                user.ban = True
                with open("database/users.json", "w", encoding='UTF-8') as json_file:
                    json.dump(all_users, json_file, indent=4, cls=UserEncoder)
                    return None
        raise UserNotFoundError