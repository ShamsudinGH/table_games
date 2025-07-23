from src.panels.state_machine.State import State

class Initial(State):
    def get_name(self) -> str:
        return "Initial"

    def run(self):
        print("Игровое меню (Админ)")
        print("[1] Игры")
        print("[2] Игроки")
        print("[0] Выход")

        action = input("Выберите действие: ")
        if action == "1":
            from src.panels.admin.states.Games import Games
            return Games()
        elif action == "2":
            from src.panels.admin.states.Gamers import Gamers
            return Gamers()
        elif action == "0":
            from src.panels.admin.states.Exit import Exit
            return Exit()
        return None