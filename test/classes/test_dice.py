import numpy.random as R

from farkle.dice import Dice


def test_dice_initalise():
    R.seed(1)  # 4
    d = Dice()
    assert d.value == 4
    assert d.is_fixed == False
    assert str(d) == "4"

    d = Dice(1, True)
    assert d.value == 1
    assert d.is_fixed == True

    assert int(d) == 1
    assert str(d) == "1!"


def test_dice_logic():
    d = Dice(3)
    assert (d == 3) == True
    assert (d == 4) == False
    assert (d != 3) == False
    assert (d >= 2) == True
    assert (d >= 4) == False
    assert (d > 2) == True
    assert (d > 3) == False
    assert (d < 4) == True
    assert (d < 3) == False
    assert (d <= 3) == True
    assert (d <= 2) == False


def test_fix_unfix():
    d = Dice()
    assert d.is_fixed == False
    d.fix()
    assert d.is_fixed == True
    d.unfix()
    assert d.is_fixed == False


def test_set_value():
    d = Dice(1)
    d.value = 2
    assert d == 2
    d.fix()
    d.value = 3
    assert d == 3


def test_roll():
    R.seed(1)
    d = Dice(1)
    d.roll()
    assert d == 4

    R.seed(1)
    d = Dice(1)
    d.fix()
    d.roll()
    assert d == 1
