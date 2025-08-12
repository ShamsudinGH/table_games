from src.components.GamerRepository import GamerRepository
from src.panels.state_machine.State import State


class Gamers(State):
    gamers_repository = GamerRepository()

    def get_name(self) -> str:
        return "Gamers"

    def run(self):
        for gamer in self.gamers_repository.get_all_gamers():
            print(f'{gamer.id}. {gamer.nickname}')
        print(f'[1] Добавить игрока \n[2] Заблокировать игрока')
        print("[0] Назад")

        action = input("Выберите действие: ")
        if action == "0":
            from src.panels.admin.states.Initial import Initial
            return Initial()
        elif action == "1":
            from src.panels.admin.states.AddGamer import AddGamer
            return AddGamer()
        elif action == "2":
            from src.panels.admin.states.BanUser import BanUser
            return BanUser()

        return None