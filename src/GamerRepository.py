# Компонент игроки
from src.model.Gamer import Gamer, create_common_gamer
from src.model.encoders.GamerEncoder import GamerEncoder
from src.model.errors.UserNotFoundError import UserNotFoundError
from src.model.errors.GamerAvailableError import GamerAvailableError
from src.utils.JsonHelper import JsonHelper
from src.utils.ListHelper import last_item


class GamerRepository:
    json_helper = JsonHelper()

    def __get_all_gamers(self) -> list[Gamer]:
        return self.json_helper.read_list_from_json("database/gamers.json", Gamer)

    def search_gamer_by_id(self, game_id) -> Gamer:
        # Загружаем список игроков из БД
        gamers = self.__get_all_gamers()
        for gamer in gamers:
            if gamer.id == game_id:
                return gamer
        # Если игрока не нашли, то выбрасываем ошибку
        raise UserNotFoundError

    def search_gamer_by_name(self, user_name) -> Gamer:
        # Загружаем список игроков из БД
        gamers = self.__get_all_gamers()
        for gamer in gamers:
            if gamer.gamer_name == user_name:
                # Если логин и пароль пользователя совпадает с тем что мы передали, то возвращаем id
                return gamer
        # Если пользователя не нашли, то выбрасываем ошибку
        raise UserNotFoundError

    def append_gamer(self, gamer_name) -> str:
        all_gamers = self.__get_all_gamers()
        for gamer in all_gamers:
            if gamer.gamer_name == gamer_name:
                raise GamerAvailableError(gamer_name)
        last_gamer = last_item(all_gamers)
        new_gamer_data = create_common_gamer(last_gamer.id + 1, gamer_name)
        all_gamers.append(new_gamer_data)
        self.json_helper.update_json("database/gamers.json", all_gamers, GamerEncoder)
        return gamer_name