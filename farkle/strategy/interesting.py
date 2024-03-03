import numpy as np
from farkle.strategy.base import DefaultStrategy
from farkle.strategy.basic import EndOn4Strategy


class EndOn45ScoreDep(DefaultStrategy):
    def onSingleScore(self):
        if self.current_turn_score < 300:
            self.END_ON_X_DICE = 6
        elif self.current_turn_score < 400:
            self.END_ON_X_DICE = 5
        else:
            self.END_ON_X_DICE = 4

        return super().onSingleScore()


class RerollForTripletsMax1(DefaultStrategy):
    def onSingleScore(self):
        # IF already scored 3 dice,
        # do not apply strategy
        if self.hand.n_fixed >= 3:
            return super().onSingleScore()

        # Strategy takes at most 1 dice before 3 dice to allow for triplet reroll
        ones_score = 0
        fives_score = 0
        if self.roll_score.ones:
            ones_score = int(self.roll_score.ones.value / self.roll_score.ones.count)
            self.hand.fix(self.roll_score.ones.idxs[:1])

        elif self.roll_score.fives:
            fives_score = int(self.roll_score.fives.value / self.roll_score.fives.count)
            self.hand.fix(self.roll_score.fives.idxs[:1])

        return ones_score + fives_score


class RerollForTripletsFill(DefaultStrategy):
    def onSingleScore(self):
        prev_fixed = self.hand.n_fixed
        # IF already scored 3 dice,
        # OR prev scored + new dice is 3 or less
        # do not apply strategy
        if prev_fixed >= 3 or prev_fixed + self.roll_score.single_scoring_count <= 3:
            return super().onSingleScore()

        def takeNsingle(have, provided):
            return min(provided, min(provided + have, 3 - have))

        ones_score = 0
        fives_score = 0

        # THIS TAKES ALL DICE TO FILL UPTO 3 SLOTS to allow for 1 triplet reroll
        if self.roll_score.ones:
            n_ones = self.roll_score.ones.count
            n_take = takeNsingle(prev_fixed, n_ones)
            if n_take == n_ones:
                ones_score = super().on1Score()
            else:
                ones_score = int((self.roll_score.ones.value / n_ones) * n_take)
                self.hand.fix(self.roll_score.ones.idxs[:n_take])

        if self.roll_score.fives:
            n_fives = self.roll_score.fives.count
            n_take = takeNsingle(self.hand.n_fixed, n_fives)
            if n_take == n_fives:
                fives_score = super().on5Score()  # never hit!
            else:
                fives_score = int((self.roll_score.fives.value / n_fives) * n_take)
                self.hand.fix(self.roll_score.fives.idxs[:n_take])

        return ones_score + fives_score
