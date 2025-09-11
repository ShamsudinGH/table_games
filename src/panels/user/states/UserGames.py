from src.components.GameRepository import GameRepository
from src.panels.state_machine.State import State


class Games(State):
    games_repository = GameRepository()

    def get_name(self) -> str:
        return "UserGames"

    def run(self):
        for game in self.games_repository.get_all_games():
            print(f'{game.id}. {game.game_name} - {game.game_price}руб')
        print("[0] Назад")

        action = input("Выберите действие: ")
        if action == "0":
            from src.panels.user.states.UserInitial import UserInitial
            return UserInitial()
        return None