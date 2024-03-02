import numpy.random as R

from farkle.turn import TestTurn
from farkle.hand import Hand
from farkle.strategy.basic import LeaveTriplet2sStrategy

def test_two_dice_then_trip():
    R.seed(2)
    t = TestTurn(Hand([2, 5, 5, 3, 4, 4]),strategy=LeaveTriplet2sStrategy())
    t.play(noroll=True, next_hand=[2, 2, 2, 4], roll_limit=2)
    assert t.score == [100,200]
    assert t.hand.fixes == [1, 1, 1, 0, 1, 1]

def test_one_dice_then_trip_plus_1():
    R.seed(2)
    t = TestTurn(Hand([2, 5, 3, 3, 4, 4]),strategy=LeaveTriplet2sStrategy())
    t.play(noroll=True, next_hand=[6, 2, 2, 2, 5], roll_limit=2)
    assert t.score == [50,50]
    assert t.hand.fixes == [0, 0, 0, 1, 1, 0] # takes single

def test_one_dice_then_trip_threes():
    R.seed(2)
    t = TestTurn(Hand([2, 5, 3, 3, 4, 4]),strategy=LeaveTriplet2sStrategy())
    t.play(noroll=True, next_hand=[6, 3, 3, 3, 5], roll_limit=2)
    assert t.score == [50,350]
    assert t.hand.fixes == [1, 1, 1, 1, 1, 0]

def test_three_dice_then_trip():
    R.seed(2)
    t = TestTurn(Hand([1, 5, 5, 3, 4, 4]),strategy=LeaveTriplet2sStrategy())
    t.play(noroll=True, next_hand=[1, 2, 2, 2], roll_limit=2)
    assert t.score == [200,200]
    assert t.has_hot_diced == True
