import pytest
import numpy as np

from farkle.scoring import ScoreElement, singleScore
from farkle.hand import Hand


def test_score_elem_initialise():
    s = ScoreElement(0)
    assert s.value == 0
    assert all(s.idxs == [-1])
    assert s.count == 0
    assert s.dice_value == -1
    s = ScoreElement(1, idxs=[1, 1])
    assert isinstance(s.idxs, np.ndarray)


def test_reset():
    s = ScoreElement(1000, 6, [1, 1, 1, 1, 1, 1], 4)
    s.reset()
    assert s.value == 0
    assert all(s.idxs == [-1])
    assert s.count == 0
    assert s.dice_value == -1


def test_bool():
    s = ScoreElement(1000, 6, [1, 1, 1, 1, 1, 1], 4)
    assert bool(s) == True
    assert not s == False
    s.reset()
    assert bool(s) == False


def test_compare_fails():
    s1 = ScoreElement(1000, 6, [1, 1, 1, 1, 1, 1], 4)
    with pytest.raises(TypeError) as _:
        ScoreElement.compare([1], s1)


def test_compare():
    s1 = ScoreElement(1000, 6, [0, 1, 2, 3, 4, 5], 4)
    s2 = ScoreElement(1000, 6, [0, 1, 2, 3, 4, 5], 4)
    assert ScoreElement.compare(s1, s2) == True
    s2 = ScoreElement(1001, 6, [0, 1, 2, 3, 4, 5], 4)
    assert ScoreElement.compare(s1, s2) == False
    s2 = ScoreElement(1000, 7, [0, 1, 2, 3, 4, 5], 4)
    assert ScoreElement.compare(s1, s2) == False
    s2 = ScoreElement(1000, 6, [0, 1, 2, 3, 4, 5], 5)
    assert ScoreElement.compare(s1, s2) == False
    s2 = ScoreElement(1000, 6, [0, 1, 2, 3, 5], 5)
    assert ScoreElement.compare(s1, s2) == False

    s1 = ScoreElement(1000, 6, [0, 1, 2, 3, 4], 4)
    s2 = ScoreElement(1000, 6, [0, 1, 2, 3, 5], 4)
    assert ScoreElement.compare(s1, s2) == False


def test_singleScore():
    s = singleScore(Hand([1, 1, 3, 4, 5, 6]), 1)
    assert s.value == 200
    assert all(s.idxs == [0, 1])
    assert s.count == 2
    assert s.dice_value == 1

    s = singleScore(Hand([1, 1, 3, 4, 5, 6]), 5)
    assert s.value == 50
    assert all(s.idxs == [4])
    assert s.count == 1
    assert s.dice_value == 5
