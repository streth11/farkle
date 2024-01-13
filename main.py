from hand import Hand
from scoring import diceScore, Score


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
        return 0
    
    def onBigScore(self):
        self.hand.fix(self.roll_score.big.idxs)           
        return self.roll_score.big.value
    
    def onTripletScore(self):
        self.hand.fix(self.roll_score.triplet.idxs)           
        return self.roll_score.triplet.value
    
    def onSingleScore(self):
        return 2
    
    def on5Score(self):
        return 5
    
    def on1Score(self):
        return 1


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
        self.roll_score = Score.dice(self.hand)
        self.executeStrategy()
        return self

    def executeStrategy(self):
        self.__strategy.update_score(self.hand, self.roll_score)
        prev_fixed = self.hand.n_fixed

        if self.roll_score.total == 0:
            score = self.__strategy.onNoScore()
        if self.roll_score.big.value:
            score = self.__strategy.onBigScore()

        print(self.roll_score.potentialScoringDice())

        if self.hand.n_fixed == 6:
            self.score.append(score)
            if score == 0:
                return self
            # hot dice
            # self.play()

        if self.roll_score.triplet.value:
            score = self.__strategy.onTripletScore()

        # farkle
        new_fixed = self.hand.n_fixed
        if prev_fixed == new_fixed:
            score = 0

        return self


if __name__ == "__main__":
    h = Hand([3,3,3,3,3,5])
    # print(h)
    # h.roll()
    # print(h.count_dict)
    # print(h.count_of_counts)
    # print(h.fixes)
    # print(h.n_fixed)

    t = Turn(h)
    t.play()

    print(h)

    x=1
