from src.panels.state_machine.State import State


class EditGame(State):

    def get_name(self) -> str:
        return "Edit_Game"