import numpy as np

from hand import Hand


def diceScore(dice: Hand):
    score = [0]

    big_score = bigDiceScore(dice)
    if big_score > 0:
        score.append(big_score)
    
    # single scores
    DICE_SCORES = [100,0,0,0,50,0]
    score = np.array(score)
    for idx,d in enumerate(dice()):
        score[1,idx] = DICE_SCORES[d-1]

    score.sort()
    
    print(score)
    return score

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

    DICE3_SCORES = [1000,200,300,400,500,600]
    if dice.n_fixed <= 3:
        if dice.count_of_counts["3 of a kinds"] == 1:
            # 3 of a kind
            dice_num_3kind_idx = (np.where(dice.count_list == 3))[0][0]+1
            dice.fix(np.where(dice.dice_array == dice_num_3kind_idx)[0])
            return DICE3_SCORES[dice_num_3kind_idx]
        
    return 0
