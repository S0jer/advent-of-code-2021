import collections
import itertools
from copy import deepcopy

position = [3, 7]
winners = [0, 0]


def play(position):
    score = [0, 0]
    done, die = False, 0
    playerID, cnt = 0, 0
    while not done:
        die += 1
        if die > 100:
            die = 1
        playerID, move = playerID % 2, die

        for _ in range(2):
            die += 1
            if die > 100:
                die = 1
            move += die

        position[playerID] = flatten(position[playerID] + move)
        score[playerID] += position[playerID]
        print(position[playerID])
        if score[playerID] >= 1000:
            done = True
        playerID += 1
        cnt += 3

    return score, cnt


def flatten(add: int) -> int:
    while add > 10:
        add -= 10
    return add

die_rolls = collections.Counter(
        i + j + k for i in (1, 2, 3) for j in (1, 2, 3) for k in (1, 2, 3)
    )

def playThree(p1: int, p1_score: int, p2: int, p2_score: int):
    p1_wins = p2_wins = 0
    for k, ct in die_rolls.items():
        new_p1 = flatten(p1 + k)
        new_p1_score = p1_score + new_p1
        if new_p1_score >= 21:
            p1_wins += ct
        else:
            tmp_p2_wins, tmp_p1_wins = playThree(p2, p2_score, new_p1, new_p1_score)

            p1_wins += tmp_p1_wins * ct
            p2_wins += tmp_p2_wins * ct

    return p1_wins, p2_wins


print(playThree(3, 0, 7, 0))
