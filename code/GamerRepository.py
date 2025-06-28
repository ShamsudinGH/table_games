import json

from code.model.errors.UserNotFoundError import UserNotFoundError
from model.Gamer import Gamer
from code.model.errors.GamerAvailableError import GamerAvailableError
from passlib.hash import pbkdf2_sha256



class GamerRepository:

    def __get_all_gamers(self):
        with open("database/gamers.json", encoding='UTF-8') as json_file:
            gamers = json.load(json_file)
            return [Gamer(**gamer) for gamer in gamers]

    def search_user(self, id):
        # Загружаем список игроков из БД
        gamers = self.__get_all_gamers()
        for gamer in gamers:
            if gamer.id == id:
                # Если логин и пароль пользователя совпадает с тем что мы передали, то возвращаем id
                return gamer
        # Если пользователя не нашли, то выбрасываем ошибку
        raise UserNotFoundError

    def append_gamer(self, gamer_name):
        all_gamers = self.__get_all_gamers()
        for gamer in all_gamers:
            if gamer.gamer_name == gamer_name:
                raise GamerAvailableError(gamer_name)
        last_gamer = all_gamers[-1]
        with open("database/gamers.json", "w", encoding='UTF-8') as json_file:
            new_gamer_data = Gamer(id=last_gamer.id+1, gamer_name=gamer_name, nickname=gamer_name, status="user")
            all_gamers.append(new_gamer_data)
            json.dump(all_gamers, json_file)
        return new_gamer_data
