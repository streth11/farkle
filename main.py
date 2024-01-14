import numpy as np

from farkle.hand import Hand
from farkle.turn import Turn

if __name__ == "__main__":

    np.random.seed(42)

    h = Hand([3,3,3,3,3,4])
    # print(h)

    t = Turn(h)
    t.play()

    print(h)
