import numpy as np

from farkle.hand import Hand
from farkle.turn import Turn

if __name__ == "__main__":

    np.random.seed(42)

    # h = Hand([2,3,3,6,4,4])
    h = Hand([3,3,3,3,3,5])
    # print(h)

    t = Turn(h)
    t.play(noroll=True,hot_dice_hand=[5,2,3,3,4,6],roll_limit=2)

    print(h)
