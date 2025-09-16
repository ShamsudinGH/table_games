import time

from src.panels.AuthorizationState import AuthorizationState
from src.panels.LogoutState import LogoutState


class SessionLifecycleHandler:
    def __init__(self, state_machine):
        self.state_machine = state_machine
        self.last_activity_time = time.time()
        self._timeout_seconds = 3

    def ping(self) -> bool:
        if type(self.state_machine.state) is AuthorizationState:
            self.__update_time__()
            return False
        elif self.__is_session_expired__():
            self.__update_time__()
            self.state_machine.change_state(LogoutState())
            return True
        else:
            self.__update_time__()
            return False

    def __is_session_expired__(self):
        current_time = time.time()
        elapsed_time = current_time - self.last_activity_time
        return elapsed_time > self._timeout_seconds

    def __update_time__(self):
        self.last_activity_time = time.time()