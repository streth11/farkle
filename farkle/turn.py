from farkle.hand import Hand
from farkle.scoring import Score
from farkle.strategy import Strategy

class Turn():
    def __init__(self, init_hand: Hand=Hand(), strategy=Strategy()) -> None:
        self.hand = init_hand
        self.__strategy = strategy
        self.roll_score = Score()
        self.score = []
        self.num_rolls = 0
    
    @property
    def totalScore(self):
        return sum(self.score)
    
    def play(self, noroll=False, hot_dice_hand=[], roll_limit=10, future_noroll=False):
        if not noroll:
            # roll dice
            self.hand.roll()
        
        # testing utilities
        if self.num_rolls >= 1 and hot_dice_hand:
            self.hand.setValues(range(0,len(hot_dice_hand)),hot_dice_hand)
        if self.num_rolls >= roll_limit:
            print(f"Roll Limit reached, score = {sum(self.score)}")
            return sum(self.score)
        
        self.num_rolls += 1
        self.hand.sortDice()
        print(self.hand)
        self.roll_score.calcualteScore(self.hand)
        saved_score = self.executeStrategy()

        self.score.append(saved_score)
        
        if self.hand.keep_and_end:
            print(self.hand)
            print(f"Turn ended, score = {sum(self.score)}")
            return sum(self.score)
        self.play(noroll=future_noroll, hot_dice_hand=hot_dice_hand, roll_limit=roll_limit)

    def executeStrategy(self):
        score = 0
        self.__strategy.update_score(self.hand, self.roll_score)

        if self.roll_score.total == 0:
            score += self.__strategy.onNoScore()

        if self.roll_score.big:
            score += self.__strategy.onBigScore()

        if self.roll_score.triplet:
            score += self.__strategy.onTripletScore()

        if self.roll_score.ones or self.roll_score.fives:
            score += self.__strategy.onSingleScore()
            
        # farkle
        if score == 0:
            self.score = []

        if self.hand.n_fixed == 6 and score > 0:
            # hot dice!
            print(f"Hot Dice!, current score = {sum(self.score)+score}")
            self.hand.keep_and_end = False
            self.hand.unfix(range(0,6))

        return score
