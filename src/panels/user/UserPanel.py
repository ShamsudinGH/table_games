from src.panels.state_machine.StateMachine import StateMachine
from src.panels.user.states.Initial import Initial


class UserPanel:
    # Карта навигации (что куда может переходить)
    source_destination_map: dict[str, list[str]] = {
        "Initial": ["Games", "Gamers", "AuthorizationState"],
        "Games": ["Initial"],
        "Gamers": ["Initial"],
        "AuthorizationState": ["Initial", "Exit"],
        "Exit": []
    }
    # Создание стейт-машины
    # initial_state - в этом параметре указываем первоначальное/изначальное/стартовое/нулевое/начальное состояние
    # source_destination_map - в этом параметре указываем карту навигации
    state_machine = StateMachine(initial_state=Initial(), source_destination_map=source_destination_map)

    def run(self):
        while True:
            print("-" * 45)
            # Запускаем текущий стейт
            new_state = self.state_machine.run_current_state()
            # Меняем текущий стейт на тот который выбрал пользователь
            self.state_machine.change_state(new_state)