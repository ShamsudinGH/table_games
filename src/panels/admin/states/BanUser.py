from src.components.UserRepository import UserRepository
from src.panels.admin.states.AdminGamers import AdminGamers
from src.panels.state_machine.State import State


class BanUser(State):
    user_repository = UserRepository()

    def get_name(self):
        return "BanUser"

    def run(self):
        ban_user_id = int(input("Введите ID пользователя: "))
        try:
            self.user_repository.ban_user(user_id=ban_user_id)
            print(f"Пользователь с ID: {ban_user_id} успешно забанен.")
        except Exception as e:
            print(e)
        print("[0] Назад")

        action = input("Выберите действие: ")
        if action == "0":
            return AdminGamers()
        return None