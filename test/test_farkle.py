import numpy.random as R

from farkle.turn import Turn
from farkle.hand import Hand

def test_5score_blank():
    t = Turn(Hand([3,3,3,3,3,2]))
    t.play(noroll=True)
    assert t.score == [2000]
    assert t.num_rolls == 1

def test_5score_five():
    t = Turn(Hand([3,3,3,3,3,5]))
    t.play(noroll=True, hot_dice_hand=[5,2,3,3,4,6], roll_limit=2)
    assert t.score == [2000+50,50]

def test_bigScore_then_another5():
    R.seed(1) # future [4,5,x,x,x,x]
    t = Turn(Hand([5,5,5,5,6,4]))
    t.play(noroll=True, future_noroll=False)
    assert t.score == [1500,50]
    assert t.num_rolls == 2

def test_bigScore_w5s():
    R.seed(2) # future [1,1,x,x,x,x], [1,2,3,3,4,4]
    t = Turn(Hand([5,5,5,5,6,4]))
    t.play(noroll=True, roll_limit=3, future_noroll=False)
    assert t.score == [1500,200,100]
