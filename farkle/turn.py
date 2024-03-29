from farkle.hand import Hand
from farkle.scoring import Score
from farkle.strategy.base import DefaultStrategy


class Turn:
    def __init__(self, init_hand: Hand = Hand(), strategy=DefaultStrategy()) -> None:
        self.hand = init_hand
        self.__strategy = strategy
        self.roll_score = Score()
        self.score = []
        self.num_rolls = 0
        self.has_hot_diced = False

    @property
    def total_score(self):
        return sum(self.score)

    def play(self, roll_limit=50):
        while not self.hand.keep_and_end:
            if self.num_rolls >= roll_limit:
                # print(f"Roll Limit reached, score = {self.total_score}")
                return self.total_score

            # roll dice
            self.hand.roll()
            self.num_rolls += 1
            self.hand.sortDice()

            # score and strategy
            self.roll_score.calcualteScore(self.hand)
            saved_score = self.executeStrategy()

            self.score.append(saved_score)

        # print(f"Turn ended, score = {self.total_score}")
        return self.total_score

    def executeStrategy(self):
        score = 0
        self.__strategy.withUpdatedScore(
            self.hand, self.roll_score, self.total_score, self.num_rolls
        )

        if self.roll_score.total == 0:
            score += self.__strategy.onNoScore()

        if self.roll_score.big:
            score += self.__strategy.onBigScore()
            self.__strategy.bigScoreResetUsedDice()

        if self.roll_score.triplet:
            score += self.__strategy.onTripletScore()
            self.__strategy.tripletScoreResetUsedDice()

        if self.roll_score.ones or self.roll_score.fives:
            score += self.__strategy.onSingleScore()

        # farkle
        if score == 0:
            self.score = []

        if self.hand.n_fixed == 6 and score > 0:
            # hot dice!
            # print(f"Hot Dice!, current score = {sum(self.score)+score}")
            self.has_hot_diced = True
            self.hand.keep_and_end = False
            self.hand.unfix(range(0, 6))

        self.__strategy.postScoreFcn()
            
        return score
