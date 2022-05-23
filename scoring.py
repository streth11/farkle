import numpy as np

# COUNT_OF_COUNT_LIST = ["nulls", "singles", "doubles", "triples", "quads", "5of"]

class DiceRoll:
    def __init__(self,dice) -> None:
        self.dice = np.array(dice)
        self.n = len(dice)

    # @property
    # def n(self) -> int:
    #     return 0 if len

    @property
    def count_list(self) -> np.array:
        return np.array([(self.dice == i).sum() for i in range(1,7)])

    @property
    def count_dict(self):
        return {i: (self.dice == i).sum() for i in range(1,7)}

    @property
    def count_of_counts(self):
        return {f"{i} of a kinds": (self.count_list == i).sum() for i in range(0,7)}

    def __call__(self) -> np.ndarray:
        return self.dice

    def __str__(self):
        return str(self.dice)


def diceScore(dice: DiceRoll):
    score = [0]
    
    if dice.n == 6:
        # scores that use all 6 dice
        if all(dice() == 1):
            # straight 1-6
            score.append(1500)
        if dice.count_of_counts["3 of a kinds"] == 2:
            # 2 triplets
            score.append(2500)
        if dice.count_of_counts["2 of a kinds"] == 3:
            # 3 pairs
            score.append(1501)
        if dice.count_of_counts["4 of a kinds"] == 1 and dice.count_of_counts["2 of a kinds"] == 1:
            # 4 of a kind and a pair (full house)
            score.append(1502)
        if dice.count_of_counts["6 of a kinds"] == 1:
            # 6 of a kind
            score.append(3000)
        non_scoring_dice = None
        if len(score) > 1:
            dice = DiceRoll([])

    if dice.n >= 5:
        if dice.count_of_counts["5 of a kinds"] == 1:
            score.append(2000)
            dice_num_5kind = (np.where(dice.count_list == 5))[0][0]+1
            dice = DiceRoll([d for d in dice() if d != dice_num_5kind])

    if dice.n >= 4:
        if dice.count_of_counts["4 of a kinds"] == 1:
            score.append(1500)
            dice_num_4kind = (np.where(dice.count_list == 4))[0][0]+1
            dice = DiceRoll([d for d in dice() if d != dice_num_4kind])

    DICE3_SCORES = [300,200,300,400,500,600]
    if dice.n >= 3:
        if dice.count_of_counts["3 of a kinds"] == 1:
            dice_num_3kind_idx = (np.where(dice.count_list == 3))[0][0]
            score.append(DICE3_SCORES[dice_num_3kind_idx])
            dice = DiceRoll([d for d in dice() if d != dice_num_3kind_idx+1])

    DICE_SCORES = [100,0,0,0,50,0]
    for d in dice():
        score.append(DICE_SCORES[d-1])

    score = np.array(score)
    score.sort()
    
    print(score)
    return score


dice = DiceRoll([2, 2, 5, 1, 1, 1])
print(dice.count_list)
print(dice.count_of_counts)

roll_score = diceScore(dice) 

