from src.panels.state_machine.State import State


class Gamers(State):
    def get_name(self) -> str:
        return "Gamers"

    def run(self):
        print("Список игроков...")
        print("[0] Назад")

        action = input("Выберите действие: ")
        if action == "0":
            from src.panels.user.states.Initial import Initial
            return Initial()
        return None