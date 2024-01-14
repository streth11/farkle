import numpy as np

from src.hand import Hand
from src.scoring import diceScore, Score

class Strategy():
    hand = None
    roll_score = 0

    @classmethod
    def update_score(cls,hand: Hand,roll_score: Score):
        cls.hand = hand
        cls.roll_score = roll_score
        return cls

    def onNoScore(self):
        self.hand.fix(range(0,6))
        self.hand.keep_and_end = True
        return 0
    
    def onFarkle(self):
        self.onNoScore()
        self.hand.keep_and_end = True
        self.roll_score.farkle()
        return 0
    
    def onBigScore(self):
        self.hand.fix(self.roll_score.big.idxs)
        if self.roll_score.big.count == 4 or self.roll_score.big.count == 5:
            self.hand.keep_and_end = True       
        return self.roll_score.big.value
    
    def onTripletScore(self):
        self.hand.fix(self.roll_score.triplet.idxs)           
        return self.roll_score.triplet.value
    
    def onSingleScore(self):
        # print(self.roll_score.potentialScoringDice())
        ones_score = 0
        fives_score = 0
        if self.roll_score.ones:
            ones_score = self.on1Score()
        if self.roll_score.fives:
            fives_score = self.on5Score()
        return ones_score + fives_score
    
    def on5Score(self):
        self.hand.fix(self.roll_score.fives.idxs)
        return self.roll_score.fives.value
    
    def on1Score(self):
        self.hand.fix(self.roll_score.fives.idxs)
        return self.roll_score.fives.value


class Turn():
    def __init__(self, init_hand: Hand=Hand(), strategy=Strategy()) -> None:
        self.hand = init_hand
        self.__strategy = strategy
        self.roll_score = Score()
        self.score = []
    
    @property
    def totalScore(self):
        return sum(self.score)
    
    def play(self):
        # self.hand.roll()
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


if __name__ == "__main__":

    np.random.seed(42)

    h = Hand([3,3,3,3,3,4])
    # print(h)

    t = Turn(h)
    t.play()

    print(h)
