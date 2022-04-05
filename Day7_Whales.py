def fuel(A):
    length = max(A) + 1
    dpLeft = [[0, 0, 0] for _ in range(length)]
    dpRight = [[0, 0, 0] for _ in range(length)]
    dp = [0] * length

    F = [0 for _ in range(length)]

    for i in A:
        F[i] += 1

    for i in range(1, length):
        if F[i - 1] != 0:
            dpLeft[i - 1][1] += F[i - 1]
            dpLeft[i - 1][2] += F[i - 1]
        dpLeft[i][0] = dpLeft[i - 1][0] + dpLeft[i - 1][2]
        dpLeft[i][1] = dpLeft[i - 1][1]
        dpLeft[i][2] = dpLeft[i - 1][2] + dpLeft[i - 1][1]

    for j in range(length - 1, 0, -1):
        if F[j] != 0:
            dpRight[j][1] += F[j]
            dpRight[j][2] += F[j]
        dpRight[j - 1][0] = dpRight[j][0] + dpRight[j][2]
        dpRight[j - 1][1] = dpRight[j][1]
        dpRight[j - 1][2] = dpRight[j][2] + dpRight[j][1]

    for a in range(length):
        dp[a] = dpLeft[a][0] + dpRight[a][0]

    return min(dp)


if __name__ == '__main__':
    with open("day7CrabTest.txt") as f:
        A = [int(x) for x in f.readline().split(',')]

    print(fuel(A))
