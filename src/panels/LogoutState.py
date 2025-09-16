from src.components.SessionManager import SessionManager
from src.panels.AuthorizationState import AuthorizationState
from src.panels.state_machine.State import State


class LogoutState(State):
    session_manager = SessionManager()

    def get_name(self) -> str:
        return "LogoutState"

    def run(self) -> 'State':
        self.session_manager.logout()
        print("Производится выход...")
        return AuthorizationState()