from src.panels.state_machine.State import State
from src.panels.state_machine.WrongStateError import WrongStateError


class StateMachine:
    state = State()
    source_destinations_map: dict[str, list[str]] = {} # Initial -> { Gamers, Games, Exit }, Gamers -> { Initial }, Games -> { Initial }, Exit -> {}

    def __init__(self, initial_state: State, source_destination_map: dict[str, list[str]]):
        self.state = initial_state
        self.source_destinations_map = source_destination_map

    def run_current_state(self) -> State:
        return self.state.run()

    def change_state(self, state: State):
        if self.__is_valid_change__(state):
            self.state = state
        else:
            raise WrongStateError

    # Метод проверки возможности изменить состояние
    def __is_valid_change__(self, new_state):
        valid_destinations = self.source_destinations_map.get(self.state.get_name()) # { Gamers, Games, Exit }
        # Содержит ли valid_destinations в себе стейт new_state.get_name()
        return valid_destinations.__contains__(new_state.get_name())
