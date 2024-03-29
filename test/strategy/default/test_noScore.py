from farkle.utility import TestTurn
from farkle.hand import Hand


def test_immediateFarkle():
    t = TestTurn(Hand([2, 3, 3, 4, 4, 6]))
    t.play(noroll=True)
    assert t.score == [0]
    assert t.num_rolls == 1


def test_hotDiceFarkle():
    t = TestTurn(Hand([3, 3, 3, 4, 4, 4]))
    t.play(noroll=True, next_hand=[2, 2, 3, 3, 4, 6])
    assert t.score == [0]
    assert t.num_rolls == 2


def test_scoreFarkle():
    t = TestTurn(Hand([1, 2, 2, 3, 3, 6]))
    t.play(noroll=True, next_hand=[2, 2, 3, 3, 4, 6])
    assert t.score == [0]
    assert t.num_rolls == 2
