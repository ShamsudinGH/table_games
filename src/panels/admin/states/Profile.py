from src.components.GamerRepository import GamerRepository
from src.components.SessionManager import SessionManager
from src.panels.state_machine.State import State


class Profile(State):
    gamer_repository = GamerRepository()
    user_id = SessionManager().get_user()

    def get_name(self) -> str:
        return "Profile"

    def run(self):
        print('Данные текущего профиля')
        print(f'ID: {self.gamer_repository.get_profile_data(self.user_id)["id"]}')
        print(f'Никнейм: {self.gamer_repository.get_profile_data(self.user_id)["nickname"]}')
        print(f"[0] Назад")

        action = input("Выберите действие: ")
        if action == "0":
            from src.panels.admin.states.AdminInitial import AdminInitial
            return AdminInitial()
        return None

