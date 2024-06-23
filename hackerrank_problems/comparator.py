# Problem Link: https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem
# Author: Dyanara Dela Rosa
# Date: January 2024

# Problem Definition: Create a comparator function wherein Players are sorted via scores in descending order.
# In case they have the same score, sort them by name in ascending order.
# In case they still have the same name, return 0 which will signify they are equal.

from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        print()

    def comparator(a, b):
        """
        Comparator function which sorts via score(desc) and name(asc).
        Parameters:
            a (Player): Player to be compared
            b (Player): Player to be compared
        Returns:
            int: Returns 1 if Player A's score is less than Player B's score,
                    if Player A's score is greater than Player B's score, return -1
                In case they have the same score:
                    Return 1 if Player A's name is lexicographically less than Player B's name;
                    if Player A's name is lexicographically greater than Player B's name return -1
                In case they have the same name:
                    return 0

        """
        # compare score in descending order
        if a.score < b.score:
            return 1
        if a.score > b.score:
            return -1
        # compare name in ascending order
        if a.name < b.name:
            return -1
        if a.name > b.name:
            return 1
        # case when two entries are the same
        return 0


n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)

# print(repr(["x","y","z"]))
# print(str(["x","y","z"]))
