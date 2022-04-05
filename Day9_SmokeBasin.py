from queue import Queue
from copy import deepcopy


def risk_level(A):
    moves = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    riskLevel, n, m = 0, len(A), len(A[0])
    for i in range(n):
        for j in range(m):
            cnt = 0
            for move in moves:
                if if_possible(i + move[0], j + move[1], n, m) and A[i][j] < A[i + move[0]][j + move[1]]:
                    cnt += 1
            if cnt == 4 or (cnt == 2 and ((i == 0 and j == 0) or (i == 0 and j == m - 1) or (i == n - 1 and j == 0) or (
                    i == n - 1 and j == m - 1))) or (cnt == 3 and ((i == 0 and (j != 0 and j != m - 1)) or
                                                                   ((i != 0 and i != n - 1) and j == m - 1) or
                                                                   (i == n - 1 and (j != 0 and j != m - 1)) or
                                                                   ((i != 0 and i != n - 1) and j == 0))):
                riskLevel += A[i][j] + 1

    return riskLevel


def risk_level_basin(A):
    moves = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    riskPlace, n, m = [], len(A), len(A[0])
    for i in range(n):
        for j in range(m):
            cnt = 0
            for move in moves:
                if if_possible(i + move[0], j + move[1], n, m) and A[i][j] < A[i + move[0]][j + move[1]]:
                    cnt += 1
            if cnt == 4:
                riskPlace.append((i, j))
            elif cnt == 2 and ((i == 0 and j == 0) or
                               (i == 0 and j == m - 1) or
                               (i == n - 1 and j == 0) or
                               (i == n - 1 and j == m - 1)):
                riskPlace.append((i, j))
            elif cnt == 3 and ((i == 0 and (j != 0 and j != m - 1)) or
                               ((i != 0 and i != n - 1) and j == m - 1) or
                               (i == n - 1 and (j != 0 and j != m - 1)) or
                               ((i != 0 and i != n - 1) and j == 0)):
                riskPlace.append((i, j))

    basin_sizes = []
    for i in riskPlace:
        G = deepcopy(A)
        basin_sizes.append(BFS(G, i))
    basin_sizes.sort(reverse=True)
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


def BFS(G, s):
    n = len(G)
    m = len(G[0])
    moves = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    Q = Queue()

    Q.put((s, G[s[0]][s[1]]))
    basin_size = 1
    while not Q.empty():
        u, last = Q.get()
        for move in moves:
            if if_possible(u[0] + move[0], u[1] + move[1], n, m) \
                    and G[u[0] + move[0]][u[1] + move[1]] >= last \
                    and G[u[0] + move[0]][u[1] + move[1]] != 9:
                basin_size += 1
                Q.put(((u[0] + move[0], u[1] + move[1]), G[u[0] + move[0]][u[1] + move[1]]))
                G[u[0] + move[0]][u[1] + move[1]] = 9
        G[u[0]][u[1]] = 9

    return basin_size


def if_possible(x, y, n, m):
    return (0 <= x and x < n and 0 <= y and y < m)


if __name__ == '__main__':
    with open("data/day9SmokeTest.txt") as f:
        A = []
        for line in f:
            A.append([int(x) for x in line.strip()])

    print(risk_level(A))
    print(risk_level_basin(A))
