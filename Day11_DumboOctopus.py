A = []
for line in open("day11OctopusTest.txt"):
    A.append([int(x) for x in line.strip()])

lights = 0

def flash(x, y):
    global lights
    lights += 1
    A[x][y] = -1
    moves, n = [(0, -1), (0, 1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)], len(A)

    for move in moves:
        xx = x + move[0]
        yy = y + move[1]
        if 0 <= xx < n and 0 <= yy < n and A[xx][yy] != -1:
            A[xx][yy] += 1
            if A[xx][yy] >= 10:
                flash(xx, yy)


n = len(A)
t = 0
while True:
    t += 1
    for x in range(n):
        for y in range(n):
            A[x][y] += 1

    for x in range(n):
        for y in range(n):
            if A[x][y] == 10:
                flash(x, y)
    done = True
    for x in range(n):
        for y in range(n):
            if A[x][y] == -1:
                A[x][y] = 0
            else:
                done = False
    if done:
        print(t)
        break
print(lights)
