from dataclasses import dataclass

from farkle.strategy.base import Strategy
from farkle.hand import Hand


def test_base_strategy():
    Strategy.__abstractmethods__ = set()

    @dataclass
    class DummyStrategy(Strategy):
        pass

    s = DummyStrategy()
    big = s.onBigScore()
    assert big == 0
    trip = s.onTripletScore()
    assert trip == 0
    no = s.onNoScore()
    assert no == 0
    sing = s.onSingleScore()
    assert sing == 0
    assert str(s) == "DummyStrategy"
