import numpy as np
import numpy.random as R

from farkle.hand import Hand
from farkle.turn import Turn
from farkle.scoring import Score

def play_farkle():
    t = Turn(Hand())
    score = t.play()
    return score, t.has_hot_diced

if __name__ == "__main__":

    np.random.seed(257473)
    n = 2000
    score_list = np.zeros(n)
    hot_dices = np.zeros(n)
    for i in range(0,n-1):
        score, h_dice = play_farkle()
        score_list[i] = score
        hot_dices[i] = h_dice

    print(hot_dices)
    print(score_list)
    
    mean_score = score_list.mean()
    print(f"Mean points: {mean_score:.4g}")
    farkle_prob = sum(score_list == 0)/n
    print(f"Probability Farkle: {farkle_prob:.4g}")
    not_hot_dice_scores = score_list[np.where((1-hot_dices)*score_list > 0)]
    mean_not_HD_score = not_hot_dice_scores.mean()
    print(f"Mean score (no F or HD): {mean_not_HD_score:.4g}")
    prob_HD_given_score = (sum(hot_dices)/n) / (1-farkle_prob)
    print(f"Prob hot dice given score: {prob_HD_given_score:.4g}")
    # hot_dice_scores = score_list[np.where(hot_dices*score_list > 0)]
