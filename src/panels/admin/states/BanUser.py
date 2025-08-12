from src.components.UserRepository import UserRepository
from src.panels.state_machine.State import State


class BanUser(State):
    user_repository = UserRepository()

    def get_name(self):
        return 'BanUser'