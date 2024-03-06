from farkle.strategy.base import DefaultStrategy

class SingleRoll(DefaultStrategy):
    def postScoreFcn(self):
        self.hand.keep_and_end = True

class EndOn5Strategy(DefaultStrategy):
    END_ON_X_DICE = 5


class EndOn4Strategy(DefaultStrategy):
    END_ON_X_DICE = 4


class LeaveTriplet2sStrategy(EndOn4Strategy):
    def onTripletScore(self):
        prev_fixed = self.hand.n_fixed
        # IF triplet is [2,2,2]
        # AND there are other scoring dice
        # AND total dice does not make hot dice
        if (
            (self.roll_score.triplet.dice_value == 2)
            and (self.roll_score.ones or self.roll_score.fives)
            and (prev_fixed + self.roll_score.single_scoring_count + 3 != 6)
        ):
            # do not take triple
            return 0

        return super().onTripletScore()
