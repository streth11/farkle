from farkle.utility import TestTurn
from farkle.hand import Hand
from farkle.strategy.interesting import RerollForTripletsFill


def test_a1_then_115():
    t = TestTurn(Hand([1, 2, 2, 3, 4, 4]), strategy=RerollForTripletsFill())
    t.play(noroll=True, next_hand=[1, 1, 5, 1, 4, 6], roll_limit=2)
    assert t.score == [100, 200]
    assert t.hand.fixes == [1, 1, 1, 0, 0, 0]


def test_1_then_155():
    t = TestTurn(Hand([1, 2, 2, 3, 4, 4]), strategy=RerollForTripletsFill())
    t.play(noroll=True, next_hand=[1, 2, 5, 1, 4, 5], roll_limit=2)
    assert t.score == [100, 150]
    assert t.hand.fixes == [1, 1, 0, 0, 1, 0]


def test_1_then_15():
    t = TestTurn(Hand([1, 2, 2, 3, 4, 4]), strategy=RerollForTripletsFill())
    t.play(noroll=True, next_hand=[1, 2, 5, 1, 4, 6], roll_limit=2)
    assert t.score == [100, 150]
    assert t.hand.fixes == [1, 1, 0, 0, 1, 0]


def test_1_then_5():
    t = TestTurn(Hand([1, 2, 2, 3, 4, 4]), strategy=RerollForTripletsFill())
    t.play(noroll=True, next_hand=[1, 2, 5, 4, 4, 6], roll_limit=2)
    assert t.score == [100, 50]
    assert t.hand.fixes == [1, 0, 0, 0, 1, 0]


def test_1_then_55():
    t = TestTurn(Hand([1, 2, 2, 3, 4, 4]), strategy=RerollForTripletsFill())
    t.play(noroll=True, next_hand=[1, 2, 5, 5, 4, 6], roll_limit=2)
    assert t.score == [100, 100]
    assert t.hand.fixes == [1, 0, 0, 1, 1, 0]


def test_11_then_11():
    t = TestTurn(Hand([1, 1, 2, 3, 4, 4]), strategy=RerollForTripletsFill())
    t.play(noroll=True, next_hand=[1, 1, 1, 1, 4, 6], roll_limit=2)
    assert t.score == [200, 100]
    assert t.hand.fixes == [1, 1, 1, 0, 0, 0]
