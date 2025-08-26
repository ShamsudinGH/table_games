from src.components.GameRepository import GameRepository
from src.panels.state_machine.State import State


class AddGame(State):
    game_repository = GameRepository()

    def get_name(self) -> str:
        return "AddGame"

    def run(self):
        new_game_name = input("Введите название новой игры: ")
        new_game_price = int(input("Введите цену новой игры: "))
        try:
            self.game_repository.append_game(new_game_name, new_game_price)
            print(f"{"-" * 45}\nИгра успешно добавлена")
        except Exception as e:
            print(e)
        print(f"[0] Назад")

        action = input("Выберите действие: ")
        if action == "0":
            from src.panels.admin.states.AdminGames import AdminGames
            return AdminGames()
        return None
