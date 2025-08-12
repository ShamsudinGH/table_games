from src.components.GamerRepository import GamerRepository
from src.panels.state_machine.State import State


class AddGamer(State):
    gamer_repository = GamerRepository()

    def get_name(self):
        return 'AddGamer'

    def run(self):


        print(f"[0] Назад")

        action = input("Выберите действие: ")
        if action == "0":
            from src.panels.admin.states.Games import Games
            return Games()
        return None
