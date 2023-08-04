# https://xkcd.com/247/

class TimeInt:
    def __init__(self):
        self.n = 100
        self.hour = 1
        self.minute = 0
        self.hour12 = 1
        self.n12 = 100

    def increment(self):
        self.minute += 1

        # Minute wrap increments hours
        if self.minute == 60:
            self.minute = 0
            self.hour += 1

        # Hour wrap resets hours
        if self.hour == 24:
            self.hour = 0
        self.hour12 = self.hour % 12  # 0 to 11
        if self.hour12 == 0:
            self.hour12 = 12

        # Set n
        self.n = self.hour * 100 + self.minute
        self.n12 = self.hour12 * 100 + self.minute


current_time = TimeInt()
for i in range(60 * 24):
    print(current_time.n, current_time.n12)
    current_time.increment()
