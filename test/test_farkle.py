import numpy.random as R

from farkle.turn import Turn
from farkle.hand import Hand

def test_5score_blank():
    t = Turn(Hand([3,3,3,3,3,2]))
    score = t.play(noroll=True)
    assert score == 2000

def test_5score_five():
    t = Turn(Hand([3,3,3,3,3,5]))
    score = t.play(noroll=True)
    assert score == 2000+50

def test_immediateFarkle():
    t = Turn(Hand([2,3,3,4,4,6]))
    score = t.play(noroll=True)
    assert score == 0
