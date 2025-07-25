from src.panels.admin.states.Initial import Initial
from src.panels.state_machine.StateMachine import StateMachine


class AdminPanel:

    source_destination_map: dict[str, list[str]] = {
        "Initial": ["Games", "Gamers", "Exit"],
        "Games": ["AddGame", "EditGame", "DeleteGame", "Initial"],
        "AddGame":["Games"],
        "EditGame":["Games"],
        "DeleteGame":["Games"],
        "Gamers": ["AddGamer", "BanUser", "Initial"],
        "AddGamer":["Gamers"],
        "BanUser":["Gamers"],
        "Exit": []
    }
    state_machine = StateMachine(initial_state=Initial(), source_destination_map=source_destination_map)

    def run(self):
        while True:
            print("-" * 45)
            new_state = self.state_machine.run_current_state()
            self.state_machine.change_state(new_state)
