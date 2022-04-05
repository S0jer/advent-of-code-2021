def SonarSweep(A):
    last_measurment = A[0]
    increases = 0

    for i in range(1, len(A)):
        if A[i] > last_measurment:
            increases += 1
        last_measurment = A[i]

    return increases


def SonarSweepWindows(A):
    last_measurment = A[0] + A[1] + A[2]
    increases = 0

    for i in range(3, len(A)):
        next_measurment = last_measurment - A[i - 3] + A[i]
        if next_measurment > last_measurment:
            increases += 1
        last_measurment = next_measurment

    return increases


if __name__ == '__main__':
    A = []
    with open('testSonarSweep.txt') as f:
        for line in f:
            A.append(int(line))

    print(SonarSweep(A))
    print(SonarSweepWindows(A))
