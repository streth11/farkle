import numpy as np

from farkle.hand import Hand
from farkle.turn import Turn

if __name__ == "__main__":

    np.random.seed(42)

    h = Hand([2,3,3,6,4,4])
    # print(h)

    t = Turn(h)
    t.play(noroll=True)

    print(h)
