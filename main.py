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
        self.roll_score = Score.dice(self.hand)
        self.executeStrategy()
        return self

    def executeStrategy(self):
        '''
        If roll_score == 0
        '''
        self.__strategy.update_score(self.hand, self.roll_score)

        if self.roll_score.total == 0:
            score = self.__strategy.onNoScore()
        if self.roll_score.big.value:
            score = self.__strategy.onBigScore()

        if self.hand.n_fixed == 6:
            self.score.append(score)
            if score == 0:
                return self
            # hot dice
            # self.play()

        if self.roll_score.triplet.value:
            score = self.__strategy.onTripletScore()

        return self


if __name__ == "__main__":
    h = Hand()
    print(h)
    h.roll()
    print(h)
    h.fix([1,2])
    print(h)
    h.sortDice()
    print(h.count_dict)
    print(h.count_of_counts)
    print(h.fixes)
    print(h.n_fixed)

    s = Score.dice(Hand([3, 3, 3, 3, 3, 1]))
    print(s)

    t = Turn(Hand([3, 3, 3, 3, 3, 1]))
    t.play()
    x=1
