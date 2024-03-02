import numpy.random as R

from farkle.turn import Turn
from farkle.hand import Hand

def test_turn_functions():
    R.seed(3)  # future [1,1,1,x,x,x], [~,~,~,1,2,4]
    t = Turn(Hand())
    s = t.play(roll_limit=3)
    assert t.score == [601, 100]
    assert s == 701
