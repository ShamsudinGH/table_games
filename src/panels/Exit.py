from src.panels.state_machine.State import State


class Exit(State):
    def get_name(self) -> str:
        return "Exit"

    def run(self):
        print("Выход")
        exit(0)