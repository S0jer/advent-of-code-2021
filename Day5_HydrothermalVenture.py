from math import inf


def hydrothermal(pairs, mini, maxi):
    if mini >= 0:
        n = maxi + 1
        m = 0
    else:
        n = maxi + 1
        m = mini * (-1)

    dp = [[0 for _ in range(m + n)] for _ in range(m + n)]

    for x in pairs:
        if x[1] == x[3]:
            for a in range(min(x[0], x[2]), max(x[0], x[2]) + 1):
                dp[a + m][x[1]] += 1
        elif x[0] == x[2]:
            for b in range(min(x[1], x[3]), max(x[1], x[3]) + 1):
                dp[x[0]][b + m] += 1
        else:
            if x[0] > x[2]:
                x[0], x[1], x[2], x[3] = x[2], x[3], x[0], x[1]
            for spot in range(x[2] - x[0] + 1 + m):
                vertical = spot if x[3] > x[1] else -spot
                horizontal = spot if x[2] > x[0] else -spot
                dp[x[0] + horizontal][x[1] + vertical] += 1

            # i_x, i_y, j_x, j_y = x[0], x[1], x[2], x[3]
            # if i_y > j_y:
            #     while i_y >= j_y:
            #         dp[i_x + m][i_y + m] += 1
            #         i_x += 1
            #         i_y -= 1
            # if i_y < j_y:
            #     while i_y <= j_y:
            #         dp[i_x + m][i_y + m] += 1
            #         i_x += 1
            #         i_y += 1

    cnt = 0
    for i in range(len(dp)):
        for j in range(len(dp)):
            if dp[i][j] > 1:
                cnt += 1

    return cnt


if __name__ == '__main__':
    pairs = []
    maxi, mini = -inf, inf
    with open("day5Test.txt") as f:
        for row in f:
            pair = []
            pair.extend([int(x) for x in row.replace(' -> ', ',').split(',')])
            if max(pair) > maxi:
                maxi = max(pair)
            if min(pair) < mini:
                mini = min(pair)
            pairs.append(pair)

    print(hydrothermal(pairs, mini, maxi))
