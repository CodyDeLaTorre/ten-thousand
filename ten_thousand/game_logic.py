import random
from collections import Counter


class GameLogic:

    @staticmethod
    def roll_dice(n):
        roll = []
        for x in range(n):
            roll.append(random.randint(1, 6))
        roll = tuple(roll)
        return roll

    @staticmethod
    def calculate_score(roll):
        current_score = 0
        roll = sorted(roll)
        # roll = [5]
        print(roll)
        counted_roll = Counter(roll)
        Counter.elements(counted_roll)
        as_list = list(counted_roll.items())
        # straight - 1,2,3,4,5,6 should return correct score
        if as_list == [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1)]:
            current_score += 1500
            as_list = []
        # three_pairs - 3 pairs should return correct score
        # if as_list is len = 3, then we know we may have 3 pairs
        if len(as_list) == 3 and as_list[1][1] == 2 and as_list[0][1] == 2:
            current_score += 1500
            as_list = []
            # two_trios - 2 sets of 3 should return correct score
            #  if as_list is len = 3, then we know we have 3 pairs
        if len(as_list) == 2 and as_list[0][1] == 3 and as_list[1][1] == 3:
            for i, j in as_list:
                if j > 2 and i == 1:
                    current_score += i * 1000 * (j - 2)
                if j > 2 and i >= 2:
                    current_score += i * 100 * (j - 2)
            return current_score
        for i, j in as_list:
            # if j is None and i == 5:
            # current_score += 50
            # zilch - roll with no scoring dice should return 0
            # ones - rolls with various number of 1s should return correct score
            # twos - rolls with various number of 2s should return correct score
            # threes - rolls with various number of 3s should return correct score
            # fours - rolls with various number of 4s should return correct score
            # fives - rolls with various number of 5s should return correct score
            # sixes - rolls with various number of 6s should return correct score
            if j == 5 and i == 1:
                current_score += i * 1000 + 1000 * 2
            elif j == 5:
                current_score += i * 100 * 2 + i * 100
            elif j == 6 and i == 1:
                current_score += 4000
            elif j == 6:
                current_score += i * 100 * 2 + i * 100 * 2
            elif j > 2 and i == 1:
                current_score += 1000 * 2 ** (j - 3)
            elif j > 2 and i >= 2:
                current_score += i * 100 * 2 ** (j - 3)
            # leftover_ones - 1s not used in set of 3 (or greater) should return correct score
            # leftover_fives - 5s not used in set of 3 (or greater) should return correct score
            elif j < 3 and i == 1:
                current_score += j * 100
            elif j < 3 and i == 5:
                current_score += j * 50
        return current_score


