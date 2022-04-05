def dive(A):
    depth = 0
    horizontal = 0
    aim = 0

    for i in range(len(A)):
        if A[i][0] == 'forward':
            horizontal += A[i][1]
            depth += aim*A[i][1]
        elif A[i][0] == 'down':
            aim += A[i][1]
        elif A[i][0] == 'up':
            aim -= A[i][1]

    return horizontal*depth






if __name__ == '__main__':
    A = []
    with open("diveTest.txt") as f:
        for line in f:
            row = line.split()
            A.append([row[0], int(row[1])])

    print(dive(A))

