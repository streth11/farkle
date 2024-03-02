from abc import ABC, abstractmethod

from farkle.hand import Hand
from farkle.scoring import Score


class BaseStrategy(ABC):
    hand = None
    roll_score = Score()

    @classmethod
    def withUpdateScore(cls, hand: Hand, roll_score: Score):
        cls.hand = hand
        cls.roll_score = roll_score
        return cls

    def onNoScore(self):
        self.hand.fix(range(0, 6))
        self.hand.keep_and_end = True
        return 0

    @abstractmethod
    def onBigScore(self):
        return 0

    def bigScoreResetUsedDice(self):
        match self.roll_score.big.dice_value:
            case -1:
                # 6 dice combo (not 6 of a kind)
                if self.roll_score.big.count == 6:
                    self.roll_score.triplet.reset()
                    self.roll_score.ones.reset()
                    self.roll_score.fives.reset()
            case 1:
                self.roll_score.ones.reset()
            case 5:
                self.roll_score.fives.reset()

    @abstractmethod
    def onTripletScore(self):
        return 0

    def tripletScoreResetUsedDice(self):
        match self.roll_score.triplet.dice_value:
            case 1:
                self.roll_score.ones.reset()
            case 5:
                self.roll_score.fives.reset()

    @abstractmethod
    def onSingleScore(self):
        return 0


class Strategy(BaseStrategy):

    def onBigScore(self):
        self.hand.fix(self.roll_score.big.idxs)
        if self.roll_score.big.count == 5:
            self.hand.keep_and_end = True

        return self.roll_score.big.value

    def onTripletScore(self):
        self.hand.fix(self.roll_score.triplet.idxs)

        return self.roll_score.triplet.value

    def onSingleScore(self):
        ones_score = 0
        fives_score = 0
        prev_fixed = self.hand.n_fixed
        if self.roll_score.ones:
            ones_score = self.on1Score()
        if self.roll_score.fives:
            fives_score = self.on5Score()

        if prev_fixed + self.roll_score.ones.count + self.roll_score.fives.count >= 5:
            self.hand.keep_and_end = True

        return ones_score + fives_score

    def on5Score(self):
        self.hand.fix(self.roll_score.fives.idxs)
        return self.roll_score.fives.value

    def on1Score(self):
        self.hand.fix(self.roll_score.ones.idxs)
        return self.roll_score.ones.value
