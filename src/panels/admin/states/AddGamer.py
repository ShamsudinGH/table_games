from src.components.GamerRepository import GamerRepository
from src.components.UserRepository import UserRepository
from src.panels.admin.states.AdminGamers import AdminGamers
from src.panels.state_machine.State import State


class AddGamer(State):
    gamer_repository = GamerRepository()
    user_repository = UserRepository()

    def get_name(self):
        return 'AddGamer'

    def run(self):
        new_gamers_name = input("Введите имя нового игрока: ")
        try:
            self.gamer_repository.append_gamer(new_gamers_name)
            user_login = input("Введите логин пользователя: ")
            user_password = input("Введите пароль пользователя: ")
            self.user_repository.append_user(user_login, user_password)
            print("Пользователь успешно добавлен")
        except Exception as e:
            print(e)
        print(f"[0] Назад")

        action = input("Выберите действие: ")
        if action == "0":
            return AdminGamers()
        return None
