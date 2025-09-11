import time


class Timer:
    def __init__(self):
        self.last_activity_time = time.time()
        self.timeout_seconds = 10

    def new_time(self):
        self.last_activity_time = time.time()

    def time_has_passed(self):
        current_time = time.time()
        elapsed_time = current_time - self.last_activity_time
        return elapsed_time > self.timeout_seconds