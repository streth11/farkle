import numpy as np
import time

from farkle.hand import Hand
from farkle.turn import Turn
from farkle.strategy.base import Strategy,DefaultStrategy
from farkle.strategy.basic import EndOn4Strategy, EndOn5Strategy, LeaveTriplet2sStrategy
from farkle.strategy.interesting import EndOn45ScoreDep, RerollForTripletsMax1, RerollForTripletsFill

class BestStrategy(RerollForTripletsMax1, LeaveTriplet2sStrategy, EndOn4Strategy):
    pass

def play_farkle(strategy: Strategy, **kwargs):
    t = Turn(Hand(), strategy)
    score = t.play(**kwargs)
    return score, t.has_hot_diced


def run_strategy(n, strategy: Strategy=DefaultStrategy(), seed=None, **kwargs):
    if seed is not None:
        np.random.seed(seed)

    score_list = np.zeros(n)
    hot_dices = np.zeros(n)
    for i in range(0, n):
        score, h_dice = play_farkle(strategy, **kwargs)
        score_list[i] = score
        hot_dices[i] = h_dice

    # print(hot_dices)
    print(score_list)

    print(f"Strategy: {strategy}")

    mean_score = score_list.mean()
    print(f"Mean points: {mean_score:.4g}")
    farkle_prob = sum(score_list == 0) / n
    print(f"Probability Farkle: {farkle_prob:.5g}")
    not_hot_dice_scores = score_list[np.where((1 - hot_dices) * score_list > 0)]
    mean_not_HD_score = not_hot_dice_scores.mean()
    print(f"Mean score (no F or HD): {mean_not_HD_score:.4g}")
    prob_HD_given_score = (sum(hot_dices) / n) / (1 - farkle_prob)
    print(f"Prob hot dice given score: {prob_HD_given_score:.4g}")
    # hot_dice_scores = score_list[np.where(hot_dices*score_list > 0)]
    print("")

    return score_list


if __name__ == "__main__":

    seed = 257473
    n = 200
    t1 = time.process_time()
    run_strategy(n, seed=seed, roll_limit=1)
    print(f"Time taken = {time.process_time()-t1}")

    run_strategy(n, strategy=EndOn5Strategy(), seed=seed)
    run_strategy(n, strategy=EndOn4Strategy(), seed=seed)
    run_strategy(n, strategy=LeaveTriplet2sStrategy(), seed=seed)
    # run_strategy(n, strategy=EndOn45ScoreDep(), seed=seed)
    run_strategy(n, strategy=RerollForTripletsMax1(), seed=seed)
    run_strategy(n, strategy=RerollForTripletsFill(), seed=seed)
    run_strategy(n, strategy=BestStrategy(), seed=seed)