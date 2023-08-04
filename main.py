class TimeInt:
    def __init__(self):
        self.n = 100
        self.hour = 1
        self.minute = 0

    def increment(self):
        self.hour = (self.n + 1) // 100
        self.minute = self.n + 1 - self.hour * 100
        if self.minute == 60:
            self.minute = 0
            self.hour += 1
        self.n = self.hour * 100 + self.minute


def time_int():
    n = 99
    hour = (n + 1) // 100
    minute = n + 1 - hour * 100
    if minute == 60:
        minute = 0
        hour += 1
    yield hour * 100 + minute


current_time = TimeInt()
for i in range(100):
    print(current_time.n)
    current_time.increment()

