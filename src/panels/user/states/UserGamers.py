from src.components.GamerRepository import GamerRepository
from src.panels.state_machine.State import State


class Gamers(State):
    gamers_repository = GamerRepository()

    def get_name(self) -> str:
        return "UserGamers"

    def run(self):
        for gamer in self.gamers_repository.get_all_gamers():
            print(f'{gamer.id}. {gamer.nickname}')
        print("[0] Назад")

        action = input("Выберите действие: ")
        if action == "0":
            from src.panels.user.states.UserInitial import UserInitial
            return UserInitial()
        return None