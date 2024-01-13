import numpy as np

from hand import Hand

class ScoreElement():
    def __init__(self, value, idxs = np.array(-1)):
        self.value = value
        self.idxs = idxs

    def __bool__(self):
        if self.value > 0:
            return True
        return False

class Score():
    def __init__(self, big=ScoreElement(0), triplet=ScoreElement(0),
                 ones=ScoreElement(0), fives=ScoreElement(0)):
        self.big = big
        self.triplet = triplet
        self.ones = ones
        self.fives = fives
    
    @property
    def score_list(self):
        return [self.big.value, self.triplet.value, self.ones.value, self.fives.value]

    @property
    def total(self):
        return sum(self.score_list)
    
    def potentialScoringDice(self):
        scoring_arr = np.zeros(6)
        for d in range(0,6):
            if np.isin(d,self.big.idxs) or np.isin(d,self.triplet.idxs) or np.isin(d,self.fives.idxs) or np.isin(d,self.ones.idxs):
                scoring_arr[d] = True
        return scoring_arr

    @staticmethod
    def dice(Hand: Hand):
        return diceScore(Hand)

    def __str__(self):
        return str(self.score_list)
    
    def __call__(self):
        return self.score_list


def diceScore(dice: Hand):
    score = Score()

    score.big = bigDiceScore(dice)
    if not score.big:
        score.triplet = tripletScore(dice)
        
    score.ones = singleScore(dice, 1)
    score.fives = singleScore(dice, 5)

    return score

def singleScore(dice: Hand, dice_number):
    # single scores
    DICE_SCORES = [100,0,0,0,50,0]
    score_value = dice.count_list[dice_number-1] * DICE_SCORES[dice_number-1]
    scoring_idx = np.where(dice.dice_array == dice_number)[0]
    return ScoreElement(score_value,scoring_idx)


def tripletScore(dice: Hand):

    DICE3_SCORES = [1000,200,300,400,500,600]
    if dice.n_fixed <= 3:
        if dice.count_of_counts["3 of a kinds"] == 1:
            # 3 of a kind
            dice_num_3kind_idx = (np.where(dice.count_list == 3))[0][0]+1
            score_value = DICE3_SCORES[dice_num_3kind_idx]
            scoring_idx = np.where(dice.dice_array == dice_num_3kind_idx)[0]
            # dice.fix(scoring_idx)
            return ScoreElement(score_value,scoring_idx)
    return ScoreElement(0)


def bigDiceScore(dice: Hand):

    if dice.n_fixed == 0:
        # scores that use all 6 dice
        if all(dice.count_list == 1):
            # straight 1-6
            return ScoreElement(1500,np.arange(0,6))
        if dice.count_of_counts["3 of a kinds"] == 2:
            # 2 triplets
            return ScoreElement(2500,np.arange(0,6))
        if dice.count_of_counts["2 of a kinds"] == 3:
            # 3 pairs
            return ScoreElement(1501,np.arange(0,6))
        if dice.count_of_counts["4 of a kinds"] == 1 and dice.count_of_counts["2 of a kinds"] == 1:
            # 4 of a kind and a pair (full house)
            return ScoreElement(1502,np.arange(0,6))
        if dice.count_of_counts["6 of a kinds"] == 1:
            # 6 of a kind
            return ScoreElement(3000,np.arange(0,6))

    if dice.n_fixed <= 1:
        if dice.count_of_counts["5 of a kinds"] == 1:
            # 5 of a kind
            dice_num_5kind = (np.where(dice.count_list == 5))[0][0]+1
            scoring_idx = np.where(dice.dice_array == dice_num_5kind)[0]
            # dice.fix(scoring_idx)
            return ScoreElement(2000,scoring_idx)

    if dice.n_fixed <= 2:
        if dice.count_of_counts["4 of a kinds"] == 1:
            # 4 of a kind
            dice_num_4kind = (np.where(dice.count_list == 4))[0][0]+1
            scoring_idx = np.where(dice.dice_array == dice_num_4kind)[0]
            # dice.fix(scoring_idx)
            return ScoreElement(1500,scoring_idx)
        
    return ScoreElement(0)
