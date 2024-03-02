from farkle.turn import Turn

class TestTurn(Turn):
    __test__ = False

    def play(self, noroll=False, next_hand=[], roll_limit=50, future_noroll=False):
        while not self.hand.keep_and_end:
            if not noroll:
                # roll dice
                self.hand.roll()
            if self.num_rolls >= 1 and not future_noroll:
                self.hand.roll()

            # testing utilities
            if self.num_rolls >= 1 and next_hand:
                self.hand.setValues(range(0, len(next_hand)), next_hand)
            if self.num_rolls >= roll_limit:
                print(f"Roll Limit reached, score = {sum(self.score)}")
                return sum(self.score)

            self.num_rolls += 1
            self.hand.sortDice()
            print("pre-strat:" + str(self.hand))

            self.roll_score.calcualteScore(self.hand)
            saved_score = self.executeStrategy()

            self.score.append(saved_score)
            print("post-strat:" + str(self.hand))
            print("")
        # print(self.hand)
        # print(f"Turn ended, score = {self.total_score}")
        return self.total_score