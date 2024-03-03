from farkle.strategy.base import DefaultStrategy
from farkle.strategy.basic import EndOn4Strategy, LeaveTriplet2sStrategy


class EndOn45ScoreDep(DefaultStrategy):
    def onSingleScore(self):
        if self.current_turn_score < 300:
            self.END_ON_X_DICE = 6
        elif self.current_turn_score < 400:
            self.END_ON_X_DICE = 5
        else:
            self.END_ON_X_DICE = 4

        return super().onSingleScore()
    
class RerollForTripletsE4(LeaveTriplet2sStrategy):
    pass