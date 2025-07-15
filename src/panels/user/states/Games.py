from src.components.GameRepository import GameRepository
from src.panels.state_machine.State import State


class Games(State):
    games_repository = GameRepository()

    def get_name(self) -> str:
        return "Games"

    def run(self):
        for game in self.games_repository.get_all_games():
            print(game)
        print("[0] Назад")

        action = input("Выберите действие: ")
        if action == "0":
            from src.panels.user.states.Initial import Initial
            return Initial()
        return None