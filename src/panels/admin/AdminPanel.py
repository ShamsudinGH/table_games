from src.panels.admin.states.Initial import Initial
from src.panels.state_machine.StateMachine import StateMachine


class AdminPanel:

    source_destination_map: dict[str, list[str]] = {
        "Initial": ["Games", "Gamers", "Exit"],
        "Games": ["Add_Game", "Edit_Game", "Delete_Game", "Initial"],
        "Gamers": ["Add_Gamer", "Ban_User", "Initial"],
        "Exit": []
    }
    state_machine = StateMachine(initial_state=Initial(), source_destination_map=source_destination_map)

    def run(self):
        print("-" * 45)
        while True:
            new_state = self.state_machine.run_current_state()
            self.state_machine.change_state(new_state)
