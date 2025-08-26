from src.panels.state_machine.State import State

class AdminInitial(State):
    def get_name(self) -> str:
        return "AdminInitial"

    def run(self):
        print("Игровое меню (Админ)")
        print("[1] Игры")
        print("[2] Игроки")
        print("[3] Профиль")
        print("[0] Выход")

        action = input("Выберите действие: ")
        if action == "1":
            from src.panels.admin.states.AdminGames import AdminGames
            return AdminGames()
        elif action == "2":
            from src.panels.admin.states.AdminGamers import AdminGamers
            return AdminGamers()
        elif action == "3":
            from src.panels.admin.states.Profile import Profile
            return Profile()
        elif action == "0":
            from src.panels.LogoutState import LogoutState
            return LogoutState()
        return None