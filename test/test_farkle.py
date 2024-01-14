import numpy.random as R

from farkle.turn import Turn
from farkle.hand import Hand

def test_5score_blank():
    R.seed(10)
    t = Turn(Hand([3,3,3,3,3,2]))
    score = t.play()
    assert score == 2000

def test_5score_five():
    R.seed(10)
    t = Turn(Hand([3,3,3,3,3,5]))
    score = t.play()
    assert score == 2000+50
