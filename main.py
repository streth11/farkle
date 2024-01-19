import numpy as np
import numpy.random as R

from farkle.hand import Hand
from farkle.turn import Turn
from farkle.scoring import Score

def play_farkle():
    t = Turn(Hand())
    score = t.play()
    return score

if __name__ == "__main__":

    score_list = []
    np.random.seed(257473)
    n = 2000
    for i in range(1,n):
        score = play_farkle()
        score_list.append(score)

    print(score_list)
    mean_score = np.mean(score_list)
    print(f"Mean: {mean_score}")