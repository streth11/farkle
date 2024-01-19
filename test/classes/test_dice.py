import numpy as np
import numpy.random as R

from farkle.dice import Dice

def test_dice_initalise():
    R.seed(1) # 4
    d = Dice()
    assert d.value == 4
    assert d.is_fixed == False