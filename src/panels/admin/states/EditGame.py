from src.components.GameRepository import GameRepository
from src.panels.state_machine.State import State


class EditGame(State):
    game_repository = GameRepository()

    def get_name(self) -> str:
        return "EditGame"

    def run(self):
        editable_game = int(input("Введите id редактируемой игры: "))
        try:
            self.game_repository.search_game_by_id(editable_game)
            new_game_name = input("Введите новое название игры: ")
            new_game_price = int(input("Введите новую цену игры: "))
            self.game_repository.edit_game(editable_game, new_game_name, new_game_price)
            print(f"{"-" * 45}\nИгра успешно изменена")
        except Exception as e:
            print(e)
        print(f"[0] Назад")

        action = input("Выберите действие: ")
        if action == "0":
            from src.panels.admin.states.Games import Games
            return Games()
        return None