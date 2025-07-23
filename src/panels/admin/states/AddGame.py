from sys import exception

from src.components.GameRepository import GameRepository
from src.model.errors import GameAlreadyExistsError
from src.panels.state_machine.State import State


class AddGame(State):
    game_repository: GameRepository()

    def get_name(self) -> str:
        return "AddGame"

    def run(self) -> None:
        new_game_name = input("Введите название новой игры: ")
        new_game_price = int(input("Введите цену новой игры: "))
        try:
            self.game_repository.append_game(new_game_name, new_game_price)
        except GameAlreadyExistsError as e :
            print(e)

