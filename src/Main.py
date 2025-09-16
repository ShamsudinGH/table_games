from src.panels.AuthorizationState import AuthorizationState
from src.panels.admin.navigation_graph import ADMIN_NAVIGATION_GRAPH
from src.panels.basic.navigation_graph import BASIC_NAVIGATION_GRAPH
from src.panels.state_machine.StateMachine import StateMachine
from src.panels.user.navigation_graph import USER_NAVIGATION_GRAPH


source_destination_map = {
    **ADMIN_NAVIGATION_GRAPH,
    **USER_NAVIGATION_GRAPH,
    **BASIC_NAVIGATION_GRAPH,
}

state_machine = StateMachine(initial_state=AuthorizationState(),
                             source_destination_map=source_destination_map)
while True:
    print("-" * 45)
    new_state = state_machine.run_current_state()
    state_machine.change_state(new_state)