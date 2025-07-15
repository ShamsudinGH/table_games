from src.panels.state_machine.StateMachine import StateMachine
from src.panels.user.states.Initial import Initial


class UserPanel:
    source_destination_map: dict[str, list[str]] = {
        "Initial": ["Games", "Gamers", "Exit"],
        "Games": ["Initial"],
        "Gamers": ["Initial"],
        "Exit": []
    }
    state_machine = StateMachine(initial_state=Initial(), source_destination_map=source_destination_map)

    def run(self):
        while True:
            print("-" * 45)
            new_state = self.state_machine.run_current_state()
            self.state_machine.change_state(new_state)