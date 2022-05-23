import numpy as np

#4645

np.random.seed(465)

num_dice = 6

class turn:
    def __init__(self) -> None:
        
        self.rolled_dice = []
        self.scored_rolls = []
        self.turn_score = 0


        self.roll()

    def roll(self,num_dice = 6):
        self.rolled_dice = np.array(np.random.randint(1,6,num_dice))
        print(self.rolled_dice)


t1 = turn()