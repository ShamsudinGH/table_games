from src.components.SessionManager import SessionManager
from src.panels.AuthorizationState import AuthorizationState
from src.panels.state_machine.State import State


class LogoutState(State):
    session_manager = SessionManager()
    def __init__(self, current_state=None):
        self.current_state = current_state

    def get_name(self) -> str:
        return "LogoutState"

    def run(self) -> 'State':
        if self.current_state is None:
            self.session_manager.logout()
            print("Производится выход...")
            return AuthorizationState()
        else:
            print("Время ожидания истекло...")
            return AuthorizationState(self.current_state)