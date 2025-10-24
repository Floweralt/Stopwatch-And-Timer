import time

class Timer:
    def __init__(self, duration):
        self.duration = duration
        self.start_time = 0
        self.running = False

    def start(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True

    def stop(self):
        if self.running:
            self.running = False

    def reset(self, duration):
        self.duration = duration
        self.start_time = 0
        self.running = False

    def remaining_time(self):
        if self.running:
            elapsed_time = time.time() - self.start_time
            return max(0, self.duration - elapsed_time)
        return self.duration
