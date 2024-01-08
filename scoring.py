import numpy as np

from hand import Hand

class Score():
    def __init__(self, big=0, triplet=0, ones=0, fives=0):
        self.big = big
        self.triplet = triplet
        self.ones = ones
        self.fives = fives
    
    @property
    def score_list(self):
        return [self.big, self.triplet, self.ones, self.fives]
    
    @property
    def total(self):
        return sum(self.score_list)
    
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
    score.triplet = tripletScore(dice)
                 
    DICE_SCORES = [100,0,0,0,50,0]
    score.ones = singleScore(dice, 1, DICE_SCORES)
    score.fives = singleScore(dice, 5, DICE_SCORES)

    return score


def singleScore(dice: Hand, dice_number, dice_scores = [100,0,0,0,50,0]):
    # single scores
    score = dice.count_list[dice_number-1] * dice_scores[dice_number-1]
    return score

def tripletScore(dice: Hand):

    DICE3_SCORES = [1000,200,300,400,500,600]
    if dice.n_fixed <= 3:
        if dice.count_of_counts["3 of a kinds"] == 1:
            # 3 of a kind
            dice_num_3kind_idx = (np.where(dice.count_list == 3))[0][0]+1
            dice.fix(np.where(dice.dice_array == dice_num_3kind_idx)[0])
            return DICE3_SCORES[dice_num_3kind_idx]
    return 0

def bigDiceScore(dice: Hand):

    if dice.n_fixed == 0:
        # scores that use all 6 dice
        if all(dice.count_list == 1):
            # straight 1-6
            dice.fix(range(0,6))
            return 1500
        if dice.count_of_counts["3 of a kinds"] == 2:
            # 2 triplets
            dice.fix(range(0,6))
            return 2500
        if dice.count_of_counts["2 of a kinds"] == 3:
            # 3 pairs
            dice.fix(range(0,6))
            return 1501
        if dice.count_of_counts["4 of a kinds"] == 1 and dice.count_of_counts["2 of a kinds"] == 1:
            # 4 of a kind and a pair (full house)
            dice.fix(range(0,6))
            return 1502
        if dice.count_of_counts["6 of a kinds"] == 1:
            # 6 of a kind
            dice.fix(range(0,6))
            return 3000

    if dice.n_fixed <= 1:
        if dice.count_of_counts["5 of a kinds"] == 1:
            # 5 of a kind
            dice_num_5kind = (np.where(dice.count_list == 5))[0][0]+1
            dice.fix(np.where(dice.dice_array == dice_num_5kind)[0])
            return 2000

    if dice.n_fixed <= 2:
        if dice.count_of_counts["4 of a kinds"] == 1:
            # 4 of a kind
            dice_num_4kind = (np.where(dice.count_list == 4))[0][0]+1
            dice.fix(np.where(dice.dice_array == dice_num_4kind)[0])
            return 1500
        
    return 0
