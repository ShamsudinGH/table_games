from src.components.GameRepository import GameRepository
from src.panels.admin.states.Games import Games
from src.panels.state_machine.State import State


class DeleteGame(State):
    game_repository = GameRepository()

    def get_name(self) -> str:
        return "DeleteGame"

    def run(self):
        game_to_be_deleted = int(input("Введите id удаляемой игры: "))
        try:
            self.game_repository.delete_game(game_to_be_deleted)
        except Exception as e:
            print(e)
        return Games()
