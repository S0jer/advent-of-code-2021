with open("day15ChitonTest.txt") as f:
    A = []
    for line in f:
        A.append([int(x) for x in line.strip('\n')])

width = len(A)
n, m = len(A), len(A[0])

for i in range(n):
    for j in range(4 * m):
        A[i].append(0)

for z in range(4 * n):
    A.append([0 for _ in range(5 * m)])

n, m = len(A), len(A[0])

for x in range(width):
    for y in range(width, m):
        if A[x][y - width] + 1 > 9:
            A[x][y] = 1
        else:
            A[x][y] = A[x][y - width] + 1

for y in range(m):
    for x in range(width, n):
        if A[x - width][y] + 1 > 9:
            A[x][y] = 1
        else:
            A[x][y] = A[x - width][y] + 1

dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(1, n):
    dp[i][0] = dp[i - 1][0] + A[i][0]
for j in range(1, m):
    dp[0][j] = dp[0][j - 1] + A[0][j]

for x in range(1, n):
    for y in range(1, m):
        dp[x][y] = A[x][y] + min(dp[x - 1][y], dp[x][y - 1])

print(dp[n - 1][m - 1])
for z in range(40):
    print(z)
    for x in range(n):
        for y in range(m):
            if 0 < x < n - 1 and 0 < y < m - 1:
                dp[x][y] = A[x][y] + min(dp[x - 1][y], dp[x][y - 1], dp[x + 1][y], dp[x][y + 1], dp[x][y] - A[x][y])
            elif x == 0 and y == m - 1:
                dp[x][y] = A[x][y] + min(dp[x][y - 1], dp[x + 1][y], dp[x][y] - A[x][y])
            elif x == n - 1 and y == m - 1:
                dp[x][y] = A[x][y] + min(dp[x - 1][y], dp[x][y - 1], dp[x][y] - A[x][y])
            elif x == n - 1 and y == 0:
                dp[x][y] = A[x][y] + min(dp[x - 1][y], dp[x][y + 1], dp[x][y] - A[x][y])

            elif x == 0 and 0 < y < m - 1:
                dp[x][y] = A[x][y] + min(dp[x][y - 1], dp[x + 1][y], dp[x][y + 1], dp[x][y] - A[x][y])
            elif x == n - 1 and 0 < y < m - 1:
                dp[x][y] = A[x][y] + min(dp[x - 1][y], dp[x][y - 1], dp[x][y + 1], dp[x][y] - A[x][y])
            elif 0 < x < n - 1 and y == 0:
                dp[x][y] = A[x][y] + min(dp[x - 1][y], dp[x + 1][y], dp[x][y + 1], dp[x][y] - A[x][y])
            elif 0 < x < n - 1 and y == m - 1:
                dp[x][y] = A[x][y] + min(dp[x - 1][y], dp[x][y - 1], dp[x + 1][y], dp[x][y] - A[x][y])

print(dp[n - 1][m - 1])
