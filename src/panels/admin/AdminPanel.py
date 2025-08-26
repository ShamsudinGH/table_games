from src.panels.admin.states.AdminInitial import AdminInitial
from src.panels.state_machine.StateMachine import StateMachine


class AdminPanel:

    source_destination_map: dict[str, list[str]] = {
        "Initial": ["Games", "Gamers", "Profile", "Exit"],
        "Games": ["AddGame", "EditGame", "DeleteGame", "Initial"],
        "AddGame":["Games"],
        "EditGame":["Games"],
        "DeleteGame":["Games"],
        "Gamers": ["AddGamer", "BanUser", "Initial"],
        "AddGamer":["Gamers"],
        "BanUser":["Gamers"],
        "Profile":["Initial"],
        "Exit": []
    }
    state_machine = StateMachine(initial_state=AdminInitial(), source_destination_map=source_destination_map)

    def run(self):
        while True:
            print("-" * 45)
            new_state = self.state_machine.run_current_state()
            self.state_machine.change_state(new_state)
