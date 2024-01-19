import numpy as np
import numpy.random as R

from farkle.hand import Hand
from farkle.dice import Dice

def test_hand_initalise():
    h = Hand()
    assert h.values == [0,0,0,0,0,0]

    init_val = [1,2,3]
    h = Hand(init_val)
    assert h.values == [1,2,3,0,0,0]

    init_val = [1,2,3,4,4,6]
    h = Hand(init_val)
    assert h.values == init_val
    assert len(h.dice_array) == 6
    assert type(h[0]) is Dice
    assert isinstance(h.dice_array, np.ndarray)
    assert h.keep_and_end == False
    h.fix([0])
    assert str(h) == "['1!', '2', '3', '4', '4', '6']"

def test_set_values():
    h = Hand()
    h.setValues([0,1],[1,2])
    assert h.values == [1,2,0,0,0,0]

def test_hand_fixes():
    init_val = [1,2,3,4,4,6]
    h = Hand(init_val)
    assert h.fixes == [False for _ in range(0,6)]
    assert h.n_fixed == 0
    h.fix([0,1,5])
    assert h.fixes == [True, True, False, False, False, True]
    assert h.n_fixed == 3

def test_hand_unfixes():
    init_val = [1,2,3,4,4,6]
    h = Hand(init_val)
    h.fix(range(0,6))
    assert h.fixes == [True for _ in range(0,6)]
    assert h.n_fixed == 6
    h.unfix([1,3])
    assert h.fixes == [True, False, True, False, True, True]
    assert h.n_fixed == 4

def test_hand_sort():
    h = Hand([4, 5, 1, 2, 4, 1])
    h.sortDice()
    assert h.values == [1,1,2,4,4,5]

def test_hand_roll():
    R.seed(1) # [4, 5, 1, 2, 4, 1]
    h = Hand()
    h.roll()
    assert h.values == [4, 5, 1, 2, 4, 1]

    R.seed(1) # [4, 5, 1, x,x,x]
    h = Hand()
    h.fix([0,1,5])
    h.roll()
    assert h.values == [0, 0, 4, 5, 1, 0]

def test_count_list():
    h = Hand([1,2,3,4,5,6])
    assert all(h.count_list == [1,1,1,1,1,1])
    h = Hand([6,6,6,6,6,6])
    assert all(h.count_list == [0,0,0,0,0,6])
    h = Hand([1,1,3,3,5,6])
    assert all(h.count_list == [2,0,2,0,1,1])
    h.fix(range(0,6))
    assert all(h.count_list == [2,0,2,0,1,1])

def test_avaliable_count_list():
    h = Hand([1,2,3,4,5,6])
    assert all(h.avaliable_count_list == [1,1,1,1,1,1])

    h = Hand([1,1,3,3,5,6])
    h.fix([0,1,5])
    assert all(h.avaliable_count_list == [0,0,2,0,1,0])
    h.fix(range(0,6))
    assert all(h.avaliable_count_list == [0,0,0,0,0,0])

def test_count_of_counts():
    base_dict = {f"{i} of a kinds": 0 for i in range(0,7)}
    h = Hand([1,2,3,4,5,6])
    test_dict = base_dict
    test_dict['1 of a kinds'] = 6
    assert h.count_of_counts == test_dict

    h = Hand([1,1,3,3,5,6])
    test_dict = base_dict
    test_dict['0 of a kinds'] = 2
    test_dict['1 of a kinds'] = 2
    test_dict['2 of a kinds'] = 2
    assert h.count_of_counts == test_dict
    h.fix(range(0,6))
    assert h.count_of_counts == test_dict

def test_avaliable_count_of_counts():
    base_dict = {f"{i} of a kinds": 0 for i in range(0,7)}
    h = Hand([1,2,3,4,5,6])
    test_dict = base_dict
    test_dict['1 of a kinds'] = 6
    assert h.avaliable_count_of_counts == test_dict

    h = Hand([1,1,3,3,5,6])
    h.fix([0,1,4])
    test_dict = base_dict
    test_dict['0 of a kinds'] = 4
    test_dict['1 of a kinds'] = 1
    test_dict['2 of a kinds'] = 1
    assert h.avaliable_count_of_counts == test_dict
