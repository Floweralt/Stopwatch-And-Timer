import time

class Stopwatch:
    def __init__(self):
        self.start_time = 0
        self.running = False

    def start(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True

    def stop(self):
        if self.running:
            elapsed_time = time.time() - self.start_time
            self.running = False
            return elapsed_time
        return 0

    def reset(self):
        self.start_time = 0
        self.running = False

    def elapsed(self):
        if self.running:
            return time.time() - self.start_time
        return 0
