from src.components.GameRepository import GameRepository
from src.panels.state_machine.State import State


class AdminGames(State):
    games_repository = GameRepository()

    def get_name(self) -> str:
        return "AdminGames"

    def run(self):
        for game in self.games_repository.get_all_games():
            print(f'{game.id}. {game.game_name} - {game.game_price}руб')
        print(f"[1] Добавить игру\n[2] Редактировать игру\n[3] Удалить игру\n[0] Назад")

        action = input("Выберите действие: ")
        if action == "0":
            from src.panels.admin.states.AdminInitial import AdminInitial
            return AdminInitial()
        elif action == "1":
            from src.panels.admin.states.AddGame import AddGame
            return AddGame()
        elif action == "2":
            from src.panels.admin.states.EditGame import EditGame
            return EditGame()
        elif action == "3":
            from src.panels.admin.states.DeleteGame import DeleteGame
            return DeleteGame()
        return None