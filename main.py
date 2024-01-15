import numpy as np

from farkle.hand import Hand
from farkle.turn import Turn
from farkle.scoring import Score

if __name__ == "__main__":

    # np.random.seed(2)
    # future [1,1,x,x,x,x]
    t = Turn()
    t.play()

    # TODO: Invetigate case
    # ['1', '1', '2', '2', '4', '5']
    # ['1!', '1!', '2', '2', '4', '5!']
    # Turn ended, score = 250