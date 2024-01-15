from farkle.hand import Hand
from farkle.scoring import Score

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
