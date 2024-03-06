import numpy as np


class Dice:
    def __init__(self, value=None, fixed=False):
        self.value = value
        self.is_fixed = fixed
        if value is None:
            self.roll()

    def roll(self):
        if not self.is_fixed:
            self.value = np.random.randint(1, 6 + 1)
        return self

    def fix(self):
        self.is_fixed = True
        return self

    def unfix(self):
        self.is_fixed = False
        return self

    def __eq__(self, other):
        if self.value == other:
            return True
        return False

    def __lt__(self, other):
        if self.value < other:
            return True
        return False

    def __gt__(self, other):
        if self.value > other:
            return True
        return False

    def __le__(self, other):
        if self.value <= other:
            return True
        return False

    def __ge__(self, other):
        if self.value >= other:
            return True
        return False

    def __str__(self):
        if self.is_fixed:
            return str(self.value) + "!"
        return str(self.value)

    def __int__(self):
        return self.value
