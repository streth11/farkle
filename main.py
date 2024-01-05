from hand import Hand
from scoring import diceScore  

if __name__ == "__main__":
    h = Hand()
    print(h)
    h.roll()
    print(h)
    h.fix([1,2])
    print(h)
    h.sortDice()
    print(h.count_dict)
    print(h.count_of_counts)
    print(h.fixes)
    print(h.n_fixed)


    diceScore(Hand([3, 3, 3, 3, 3, 2]))
        
    # dice = DiceRoll([2, 5, 5, 1, 1, 1])
    # print(dice.count_list)
    # print(dice.count_of_counts)


