import numpy as np

from farkle.hand import Hand
from farkle.turn import TestTurn
from farkle.strategy.base import Strategy
from farkle.strategy.basic import EndOn4Strategy, EndOn5Strategy

SEED = 257473
N = 100


def play_farkle(strategy: Strategy):
    t = TestTurn(Hand(), strategy)
    score = t.play()
    return score, t.has_hot_diced


def run_strategy(n, strategy: Strategy, seed=None):
    if seed is not None:
        np.random.seed(seed)

    score_list = np.zeros(n)
    hot_dices = np.zeros(n)
    for i in range(0, n - 1):
        score, h_dice = play_farkle(strategy)
        score_list[i] = score
        hot_dices[i] = h_dice

    mean_score = score_list.mean()
    farkle_prob = sum(score_list == 0) / n
    not_hot_dice_scores = score_list[np.where((1 - hot_dices) * score_list > 0)]
    mean_not_HD_score = not_hot_dice_scores.mean()
    prob_HD_given_score = (sum(hot_dices) / n) / (1 - farkle_prob)

    return mean_score, farkle_prob, mean_not_HD_score, prob_HD_given_score


def test_EndOn4Strategy():
    mean_score, farkle_prob, mean_not_HD_score, prob_HD_given_score = run_strategy(
        N, strategy=EndOn4Strategy(), seed=SEED
    )
    assert round(mean_score, 1) == 827.8
    assert farkle_prob == 0.11
    assert round(mean_not_HD_score, 1) == 521.2
    assert round(prob_HD_given_score, 4) == 0.2247


def test_EndOn5Strategy():
    mean_score, farkle_prob, mean_not_HD_score, prob_HD_given_score = run_strategy(
        N, strategy=EndOn5Strategy(), seed=SEED
    )
    assert round(mean_score, 1) == 620.1
    assert farkle_prob == 0.43
    assert round(mean_not_HD_score, 1) == 583.4
    assert round(prob_HD_given_score, 4) == 0.4561
