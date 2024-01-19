import numpy as np

from farkle.dice import Dice

class Hand():
    def __init__(self, init_values=[]):
        self.dice_list = [Dice(init_values[i]) if i < len(init_values) else Dice(0) for i in range(0,6)]
        self.keep_and_end = False
        
    @property
    def dice_array(self):
        return np.array(self.dice_list)
    
    def roll(self):
        for d in self.dice_list:
            if not d.is_fixed: # TODO: check and remove
                d.roll()
        return self

    def fix(self,idxs):
        for idx in idxs:
            self.dice_list[idx].fix()
        return self
    
    def unfix(self,idxs):
        for idx in idxs:
            self.dice_list[idx].unfix()
        return self
    
    def setValues(self,idxs,values):
        for idx in idxs:
            self.dice_list[idx].set_value(values[idx]) 
        return self

    def sortDice(self):
        self.dice_list.sort(key=lambda d: d.value)
        return self

    @property
    def values(self):
        return [d.value for d in self.dice_list]

    @property
    def avaliable_count_list(self):
        return np.array([sum([
            1 for d in range(0,6) if self.dice_array[d] == i and not self.dice_array[d].is_fixed
            ]) for i in range(1,7)])

    @property
    def avaliable_count_of_counts(self):
        return {f"{i} of a kinds": (self.avaliable_count_list == i).sum() for i in range(0,7)}

    @property
    def count_list(self):
        return np.array([(self.dice_array == i).sum() for i in range(1,7)])

    # @property
    # def count_dict(self):
    #     return {f"{i}": (self.dice_array == i).sum() for i in range(1,7)}

    @property
    def count_of_counts(self):
        return {f"{i} of a kinds": (self.count_list == i).sum() for i in range(0,7)}
    
    @property
    def fixes(self):
        return [d.is_fixed for d in self.dice_list]
    
    @property
    def n_fixed(self):
        return sum(self.fixes)

    def __str__(self):
        return str([str(d) for d in self.dice_list])
    
    def __getitem__(self,item):
        return self.dice_list[item]
