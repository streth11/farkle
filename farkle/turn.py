from farkle.hand import Hand
from farkle.scoring import Score
from farkle.strategy import Strategy

class Turn():
    def __init__(self, init_hand: Hand=Hand(), strategy=Strategy()) -> None:
        self.hand = init_hand
        self.__strategy = strategy
        self.roll_score = Score()
        self.score = []
    
    @property
    def totalScore(self):
        return sum(self.score)
    
    def play(self, noroll=False):
        if not noroll:
            self.hand.roll()
        self.hand.sortDice()
        self.roll_score.calcualteScore(self.hand)
        saved_score = self.executeStrategy()

        self.score.append(saved_score)

        if self.hand.keep_and_end:
            print(f"Turn ended, score = {sum(self.score)}")
            return sum(self.score)
        
        self.play()

    def executeStrategy(self):
        score = 0
        self.__strategy.update_score(self.hand, self.roll_score)
        prev_fixed = self.hand.n_fixed

        if self.roll_score.total == 0:
            score += self.__strategy.onNoScore()

        if self.roll_score.big:
            score += self.__strategy.onBigScore()

        if self.roll_score.triplet:
            score += self.__strategy.onTripletScore()

        if self.roll_score.ones or self.roll_score.fives:
            score += self.__strategy.onSingleScore()
            
        # farkle
        new_fixed = self.hand.n_fixed
        if prev_fixed == new_fixed:
            score = 0

        if self.hand.n_fixed == 6:
            if score == 0:
                return 0
            #hot dice
            pass

        return score
