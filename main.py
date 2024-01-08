from hand import Hand
from scoring import diceScore, Score

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


    s = Score.dice(Hand([3, 3, 3, 3, 3, 1]))
    print(s)


