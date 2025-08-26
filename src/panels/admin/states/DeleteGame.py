from src.components.GameRepository import GameRepository
from src.panels.state_machine.State import State


class DeleteGame(State):
    game_repository = GameRepository()

    def get_name(self) -> str:
        return "DeleteGame"

    def run(self):
        game_to_be_deleted = int(input("Введите id удаляемой игры: "))
        if self.game_repository.delete_game(game_to_be_deleted):
            print(f"{"-"*45}\nИгра успешно удалена")
        else:
            print(f"{"-"*45}\nНет игры под id: {game_to_be_deleted}")
        print(f"[0] Назад")

        action = input("Выберите действие: ")
        if action == "0":
            from src.panels.admin.states.AdminGames import AdminGames
            return AdminGames()
        return None
