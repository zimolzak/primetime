# https://xkcd.com/247/

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


current_time = TimeInt()
for i in range(100):
    print(current_time.n)
    current_time.increment()
