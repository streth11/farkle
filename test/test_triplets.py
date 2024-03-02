import numpy.random as R

from farkle.turn import Turn
from farkle.hand import Hand


def test_secondTriplet():

    t = Turn(Hand([6, 6, 6, 2, 3, 4]))
    t.play(noroll=True, hot_dice_hand=[5, 5, 5], roll_limit=2)
    assert t.score == [600, 500]
    assert t.num_rolls == 2


def test_secondTriplet2():

    t = Turn(Hand([5, 5, 5, 2, 3, 4]))
    t.play(noroll=True, hot_dice_hand=[1, 1, 1], roll_limit=2)
    assert t.score == [500, 601]
    assert t.num_rolls == 2
