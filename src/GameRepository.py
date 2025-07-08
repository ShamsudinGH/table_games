# Компонент Игры
# -------------------------------------------------------
# +найти_игру(название): Игра
# +список_игр(): List<Игра>
# +удалить_игру(название)
# +добавить_игру(название, стоимость)

from src.model.Game import Game, create_common_game
from src.model.errors.GameNotFoundError import GameNotFoundError
from src.utils.JsonHelper import JsonHelper
from src.model.errors.GameAlreadyExistsError import GameAlreadyExistsError
from src.utils.ListHelper import last_item
from src.model.encoders.GameEncoder import GameEncoder


class GameRepository:

    json_helper = JsonHelper()

    def __get_all_games(self) -> list[Game]:
        return  self.json_helper.read_list_from_json("database/games.json", Game)

    def search_game(self, game_name: str) -> Game:
        games = self.__get_all_games()
        for game in games:
            if game.game_name == game_name :
                return game
        # Если игрока не нашли, то выбрасываем ошибку
        raise GameNotFoundError

    def append_game(self, game_name: str, game_price: int) -> None:
        all_games = self.__get_all_games()
        for game in all_games:
            if game.game_name == game_name:
                raise GameAlreadyExistsError(game_name)
        last_game = last_item(all_games)
        new_game_data = create_common_game(last_game.id + 1, game_name, game_price)
        all_games.append(new_game_data)
        self.json_helper.update_json("database/games.json", all_games, GameEncoder)

    def delete_game(self, game_name: str) -> None:
        all_games = self.__get_all_games()
        for game in all_games:
            if game.game_name == game_name:
                all_games.remove(game)
        self.json_helper.update_json("database/games.json", all_games, GameEncoder)
