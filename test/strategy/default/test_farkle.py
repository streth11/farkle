import numpy.random as R

from farkle.utility import TestTurn
from farkle.hand import Hand


def test_5score_blank():
    t = TestTurn(Hand([3, 3, 3, 3, 3, 2]))
    t.play(noroll=True)
    assert t.score == [2000]
    assert t.num_rolls == 1


def test_5score_five():
    t = TestTurn(Hand([3, 3, 3, 3, 3, 5]))
    t.play(noroll=True, next_hand=[5, 2, 3, 3, 4, 6], roll_limit=2)
    assert t.score == [2000 + 50, 50]


def test_bigScore_then_another5():
    R.seed(1)  # future [4,5,x,x,x,x]
    t = TestTurn(Hand([5, 5, 5, 5, 6, 4]))
    t.play(noroll=True, future_noroll=False)
    assert t.score == [1000, 50]
    assert t.num_rolls == 2


def test_bigScore_w5s():
    R.seed(2)  # future [1,1,x,x,x,x], [1,2,3,3,4,4]
    t = TestTurn(Hand([5, 5, 5, 5, 6, 4]))
    t.play(noroll=True, roll_limit=3, future_noroll=False)
    assert t.score == [1000, 200, 100]
