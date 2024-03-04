import numpy as np

from farkle.dice import Dice


class Hand:
    _d0 = Dice(0)
    _dirty = {}
    _caches = {}

    def __init__(self, init_values=[]):
        self.dice_list = [
            Dice(init_values[i]) if i < len(init_values) else Dice(0)
            for i in range(0, 6)
        ]
        self.keep_and_end = False
        self._dirty["init"] = True

    def _makesDirty(func):
        def decorator_func(self, *args, **kwargs):
            if not all(self._dirty.values()):
                self._dirty.update(dict.fromkeys(self._dirty, True))
            return func(self, *args, **kwargs)

        decorator_func.__name__ = func.__name__
        return decorator_func

    def _cached(func):
        def decorator_func(self):
            if func.__name__ not in self._dirty:
                self._dirty[func.__name__] = True

            if self._dirty[func.__name__]:
                self._dirty[func.__name__] = False

                result = func(self)
                self._caches[func.__name__] = result
            return self._caches[func.__name__]

        decorator_func.__name__ = func.__name__
        return decorator_func

    @property
    def dice_array(self):
        return np.array(self.dice_list)

    @property
    @_cached
    def avaliable_dice_array(self):
        return np.array([d if not d.is_fixed else self._d0 for d in self.dice_list])

    @_makesDirty
    def roll(self):
        for d in self.dice_list:
            d.roll()
        return self

    @_makesDirty
    def fix(self, idxs):
        for idx in idxs:
            self.dice_list[idx].fix()
        return self

    @_makesDirty
    def unfix(self, idxs):
        for idx in idxs:
            self.dice_list[idx].unfix()
        return self

    @_makesDirty
    def setValues(self, idxs, values):
        for idx in idxs:
            self.dice_list[idx].value = values[idx]
        return self

    @_makesDirty
    def sortDice(self):
        self.dice_list.sort(key=lambda d: d.value)
        return self

    @property
    @_cached
    def avaliable_count_list(self):
        return np.array(
            [sum(1 for d in self.avaliable_dice_array if d == i) for i in range(1, 7)]
        )

    @property
    @_cached
    def avaliable_count_of_counts(self):
        return {
            f"{i} of a kinds": (self.avaliable_count_list == i).sum()
            for i in range(0, 7)
        }

    @property
    def count_list(self):
        return np.array([(self.dice_array == i).sum() for i in range(1, 7)])

    @property
    def count_of_counts(self):
        return {f"{i} of a kinds": (self.count_list == i).sum() for i in range(0, 7)}

    @property
    def values(self):
        return [d.value for d in self.dice_list]

    @property
    def fixes(self):
        return [d.is_fixed for d in self.dice_list]

    @property
    def n_fixed(self):
        return sum(self.fixes)

    def __str__(self):
        return str([str(d) for d in self.dice_list])

    def __getitem__(self, item):
        return self.dice_list[item]
