def binaryDiagnostic(A):
    n = len(A[0])
    zero = [0] * n
    ones = [0] * n

    for i in A:
        for j in range(n):
            if i[j] == '1':
                ones[j] += 1
            elif i[j] == '0':
                zero[j] += 1

    gamma_rate = ''
    epsilon_rate = ''

    for z in range(n):
        if ones[z] > zero[z]:
            gamma_rate += '1'
            epsilon_rate += '0'
        elif ones[z] < zero[z]:
            gamma_rate += '0'
            epsilon_rate += '1'

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def life_supporting_rating(A):
    ones_idx, zero_idx = [], []
    ones, zero = 0, 0

    for i in range(len(A)):
        if A[i][0] == '1':
            ones += 1
            ones_idx.append(i)
        elif A[i][0] == '0':
            zero += 1
            zero_idx.append(i)

    if ones >= zero:
        oxygen = ones_idx
        co = zero_idx
    else:
        oxygen = zero_idx
        co = ones_idx

    oxygen = findOxygen(A, oxygen, 1)
    co = findCo(A, co, 1)

    return int(A[co[0]], 2) * int(A[oxygen[0]], 2)


def findOxygen(A, T, x):
    n = len(A[0])

    ones_idx, zero_idx = [], []
    ones, zero = 0, 0

    for i in T:
        if A[i][x] == '1':
            ones += 1
            ones_idx.append(i)
        elif A[i][x] == '0':
            zero += 1
            zero_idx.append(i)

    if ones >= zero:
        T = ones_idx
    else:
        T = zero_idx

    x += 1
    if len(T) < 2 or x >= n:
        return T
    else:
        return findOxygen(A, T, x)


def findCo(A, T, x):
    n = len(A[0])

    ones_idx, zero_idx = [], []
    ones, zero = 0, 0

    for i in T:
        if A[i][x] == '1':
            ones += 1
            ones_idx.append(i)
        elif A[i][x] == '0':
            zero += 1
            zero_idx.append(i)

    if zero <= ones:
        T = zero_idx
    else:
        T = ones_idx

    x += 1
    if len(T) < 2 or x >= n:
        return T
    else:
        return findCo(A, T, x)


if __name__ == '__main__':
    A = []
    with open("diagnosticTest.txt") as f:
        for line in f:
            row = line.split()
            A.append(row[0])

    print(binaryDiagnostic(A))
    print(life_supporting_rating(A))
