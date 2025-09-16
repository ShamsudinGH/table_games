from src.panels.LogoutState import LogoutState
from src.panels.state_machine.SessionLifecycleHandler import SessionLifecycleHandler
from src.panels.state_machine.State import State
from src.panels.state_machine.WrongStateError import WrongStateError


class StateMachine:
    # Текущий стейт нашей машины
    state: State = None
    # Карта навигации
    source_destinations_map: dict[str, list[str]] = {}

    # initial_state - начальный стейт машины
    # source_destination_map - карта навигации
    def __init__(self, initial_state: State, source_destination_map: dict[str, list[str]]):
        # Устанавливаем в текущий стейт значение из initial_state
        self.state = initial_state
        # Устанавливаем карту навигации
        self.source_destinations_map = source_destination_map
        # Устанавливаем слушатель сессии
        self.session_lifecycle_handler = SessionLifecycleHandler(self)

    # Запуск текущего стейта
    def run_current_state(self) -> State:
        # Вызываем метод run у текущего стейта
        return self.state.run()

    # Сменить текущий стейт на тот который передали в параметре state
    def change_state(self, new_state: State):
        # Проверка что state не равен None
        if new_state is None:
            raise WrongStateError

        if self.session_lifecycle_handler.ping():
            return

        # Проверка что навигация разрешена и время активности не прошло
        if self.__is_valid_change__(new_state):
            # Если навигация разрешена, то меняем текущий стейт на тот который выбрал пользователь
            self.state = new_state
        else:
            raise WrongStateError

    # Метод проверки возможности изменить состояние
    def __is_valid_change__(self, new_state):
        # Если новый стейт это разлогин, то разрешаем без проверки графа навигации
        if type(new_state) is LogoutState:
            return True
        # Получаем список доступных стейтов для перехода (например для стейта "Initial" будет ["Games", "Gamers"])
        valid_destinations = self.source_destinations_map.get(self.state.get_name())
        # Содержит ли valid_destinations в себе стейт new_state.get_name()
        return new_state.get_name() in valid_destinations # (Есть ли "Games" в списке ["Games", "Gamers"])
