def lantern_fish(A, days):
    dayNumber = 0

    while dayNumber < days:
        n = len(A)
        for i in range(n):
            A[i] -= 1
            if A[i] == -1:
                A[i] = 6
                A.append(8)

        dayNumber += 1

    return len(A)


def lantern_fish_smart(A, days):
    fish = [0 for _ in range(10)]
    for i in A:
        fish[i] += 1

    for i in range(days):
        add = fish[0]
        for index in range(len(fish) - 1):
            fish[index] = fish[index + 1]
        fish[6] += add
        fish[8] += add

    result = sum(fish)

    return result



if __name__ == '__main__':
    with open("data/day6LanterfishTest.txt") as f:
        A = [int(x) for x in f.readline().split(',')]

    days = 256
    print(lantern_fish_smart(A, days))
