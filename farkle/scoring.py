import numpy as np

from farkle.hand import Hand


class ScoreElement:
    def __init__(self, value, count=0, idxs=np.array(-1), dice_value=-1):
        self.value = value
        self.idxs = idxs
        if isinstance(idxs, list):
            self.idxs = np.asarray(idxs)
        self.count = count
        self.dice_value = dice_value

    def reset(self):
        self.value = 0
        self.idxs = np.array(-1)
        self.count = 0
        self.dice_value = -1

    def __bool__(self):
        if self.value > 0:
            return True
        return False

    @staticmethod
    def compare(first, second):
        if not isinstance(first, ScoreElement) or not isinstance(first, ScoreElement):
            raise TypeError("Both elements must be ScoreElement")

        value_check = first.value == second.value
        count_check = first.count == second.count
        dice_value_check = first.dice_value == second.dice_value
        if len(first.idxs) == len(second.idxs):
            idxs_check = all(first.idxs == second.idxs)
        else:
            idxs_check = False

        return value_check and count_check and dice_value_check and idxs_check


class Score:
    def __init__(
        self,
        big=ScoreElement(0),
        triplet=ScoreElement(0),
        ones=ScoreElement(0),
        fives=ScoreElement(0),
    ):
        self.big = big
        self.triplet = triplet
        self.ones = ones
        self.fives = fives

    def potentialScoringDice(self):
        scoring_arr = np.zeros(6)
        for d in range(0, 6):
            if any(np.isin(d, s) for s in self.score_list):
                scoring_arr[d] = True
        return scoring_arr

    def calcualteScore(self, hand):
        self.big = bigDiceScore(hand)
        if not self.big:
            self.triplet = tripletScore(hand)

        self.ones = singleScore(hand, 1)
        self.fives = singleScore(hand, 5)
        return self

    @property
    def score_list(self):
        return [self.big, self.triplet, self.ones, self.fives]

    @property
    def score_value_list(self):
        return [s.value for s in self.score_list]

    @property
    def single_scoring_count(self):
        return self.ones.count + self.fives.count

    @property
    def total(self):
        return sum(self.score_value_list)

    @classmethod
    def dice(cls, hand: Hand):
        return cls().calcualteScore(hand)

    def __str__(self):
        return str(self.score_value_list)

    def __call__(self):
        return self.score_list


def diceScore(hand: Hand):
    score = Score()

    score.big = bigDiceScore(hand)
    if not score.big:
        score.triplet = tripletScore(hand)

    score.ones = singleScore(hand, 1)
    score.fives = singleScore(hand, 5)

    return score


def singleScore(hand: Hand, dice_number) -> ScoreElement:
    # single scores
    DICE_SCORES = [100, 0, 0, 0, 50, 0]
    dice_count = hand.avaliable_count_list[dice_number - 1]
    score_value = dice_count * DICE_SCORES[dice_number - 1]
    scoring_idx = np.where(hand.avaliable_dice_array == dice_number)[0]
    return ScoreElement(score_value, dice_count, scoring_idx, dice_number)


def tripletScore(hand: Hand) -> ScoreElement:
    DICE3_SCORES = [601, 200, 300, 400, 500, 600]
    if hand.n_fixed <= 3:
        if hand.avaliable_count_of_counts["3 of a kinds"] == 1:
            # 3 of a kind
            dice_num_3kind = (np.where(hand.avaliable_count_list == 3))[0][0] + 1
            score_value = DICE3_SCORES[dice_num_3kind - 1]
            scoring_idx = np.where(hand.avaliable_dice_array == dice_num_3kind)[0]
            return ScoreElement(score_value, 3, scoring_idx, dice_num_3kind)
    return ScoreElement(0)


def bigDiceScore(hand: Hand) -> ScoreElement:
    if hand.n_fixed == 0:
        # scores that use all 6 hand
        if all(hand.count_list == 1):
            # straight 1-6
            return ScoreElement(1500, 6, np.arange(0, 6))
        if hand.count_of_counts["3 of a kinds"] == 2:
            # 2 triplets
            return ScoreElement(2500, 6, np.arange(0, 6))
        if hand.count_of_counts["2 of a kinds"] == 3:
            # 3 pairs
            return ScoreElement(1501, 6, np.arange(0, 6))
        if (
            hand.count_of_counts["4 of a kinds"] == 1
            and hand.count_of_counts["2 of a kinds"] == 1
        ):
            # 4 of a kind and a pair (full house)
            return ScoreElement(1502, 6, np.arange(0, 6))
        if hand.count_of_counts["6 of a kinds"] == 1:
            # 6 of a kind
            dice_num_6kind_idx = (np.where(hand.count_list == 6))[0][0] + 1
            return ScoreElement(3000, 6, np.arange(0, 6), dice_num_6kind_idx)

    if hand.n_fixed <= 1:
        if hand.avaliable_count_of_counts["5 of a kinds"] == 1:
            # 5 of a kind
            dice_num_5kind = (np.where(hand.avaliable_count_list == 5))[0][0] + 1
            scoring_idx = np.where(hand.avaliable_dice_array == dice_num_5kind)[0]
            return ScoreElement(2000, 5, scoring_idx, dice_num_5kind)

    if hand.n_fixed <= 2:
        if hand.avaliable_count_of_counts["4 of a kinds"] == 1:
            # 4 of a kind
            dice_num_4kind = (np.where(hand.avaliable_count_list == 4))[0][0] + 1
            scoring_idx = np.where(hand.avaliable_dice_array == dice_num_4kind)[0]
            return ScoreElement(1000, 4, scoring_idx, dice_num_4kind)

    return ScoreElement(0)
