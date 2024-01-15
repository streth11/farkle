import numpy.random as R

from farkle.turn import Turn
from farkle.hand import Hand

def test_5score_blank():
    t = Turn(Hand([3,3,3,3,3,2]))
    score = t.play(noroll=True)
    assert score == 2000
    assert t.num_rolls == 1


def test_5score_five():
    R.seed(1)
    t = Turn(Hand([3,3,3,3,3,5]))
    t.play(noroll=True, hot_dice_hand=[5,2,3,3,4,6], roll_limit=2)
    assert t.score == [2000+50,50]
    assert t.num_rolls == 2
