from dice import Dice

class Hand():
    def __init__(self, init_values=None):
        self.dice_list = [Dice(0) for _ in range(0,6)]
    
    def roll(self):
        for d in self.dice_list:
            if not d.is_fixed:
                d.roll()
        return self

    def fix(self,idxs):
        for idx in idxs:
            self.dice_list[idx].fix()
        return self
    
    def sortDice(self):
        self.dice_list.sort(key=lambda d: d.value)
        return self

    def values(self):
        return [d.value for d in self.dice_list]

    def fixes(self):
        return [d.is_fixed for d in self.dice_list]

    def __str__(self):
        return str([str(d) for d in self.dice_list])


                

if __name__ == "__main__":
    d = Dice()
    h = Hand()
    print(h)
    h.roll()
    print(h)
    h.fix([1,2])
    print(h)
    h.sortDice()