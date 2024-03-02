from farkle.turn import TestTurn
from farkle.hand import Hand


def test_secondTriplet():

    t = TestTurn(Hand([6, 6, 6, 2, 3, 4]))
    t.play(noroll=True, next_hand=[5, 5, 5], roll_limit=2)
    assert t.score == [600, 500]
    assert t.num_rolls == 2


def test_secondTriplet2():

    t = TestTurn(Hand([5, 5, 5, 2, 3, 4]))
    t.play(noroll=True, next_hand=[1, 1, 1], roll_limit=2)
    assert t.score == [500, 601]
    assert t.num_rolls == 2
