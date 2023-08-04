# https://xkcd.com/247/

import matplotlib.pyplot as plt


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


def prime_factors(n):
    # https://stackoverflow.com/questions/15347174/python-finding-prime-factors
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


current_time = TimeInt()
x = []
y = []
for i in range(60 * 24):
    na = current_time.n
    nb = current_time.n12
    a = prime_factors(na)
    b = prime_factors(nb)
    if len(a) == len(b) and na != nb:
        x.append(current_time.minute)
        y.append(current_time.hour12)
        print(na, nb, a, b)
    current_time.increment()

print()
print(len(x))
print(60 * 24)
print(len(x) / 60 / 24)

fig, ax = plt.subplots()
ax.scatter(x, y)
ax.set_xlabel('Minute')
ax.set_ylabel('Hour (p.m.)')
plt.show()
