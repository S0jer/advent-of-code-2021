from math import ceil

with open("data/day14PolymeryzationTest.txt") as f:
    template = ''
    pairs = []
    for line in f:
        if '->' in line:
            pairs.append([str(x) for x in line.strip().split(' -> ')])

        else:
            template += str(line.strip('\n'))


def part_one(template):
    steps = 10
    letters = [0 for _ in range(26)]
    for letter in template:
        letters[ord(letter) - 65] += 1

    for step in range(steps):
        new_template = template[0]
        for i in range(1, len(template)):
            check = template[i - 1] + template[i]
            for pair in pairs:
                if check == pair[0]:
                    letters[ord(pair[1]) - 65] += 1
                    new_template += pair[1] + template[i]

        template = new_template


def dynamic_part_two(template):
    characters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    m = 42
    dp = [[0 for _ in range(676)] for _ in range(m)]
    cnt = 0
    n = len(dp[0])
    for c1 in characters:
        for c2 in characters:
            check = c1 + c2
            found = False
            for pair in pairs:
                if pair[0] == check:
                    dp[0][cnt] = [c1 + c2, pair[1]]
                    found = True
                    break
            if not found:
                dp[0][cnt] = [c1 + c2, None]
            cnt += 1

    for i in range(1, len(template)):
        check = template[i - 1] + template[i]
        for j in range(n):
            if dp[0][j][0] == check:
                dp[1][j] += 1

    for i in range(2, m):
        for j in range(n):
            if dp[i - 1][j] != 0 and dp[0][j][1] is not None:
                added = 0
                new_char1 = dp[0][j][0][0] + dp[0][j][1]
                new_char2 = dp[0][j][1] + dp[0][j][0][1]
                for a in range(n):
                    if dp[0][a][0] == new_char1:
                        added += 1
                        dp[i][a] += dp[i - 1][j]
                    if dp[0][a][0] == new_char2:
                        added += 1
                        dp[i][a] += dp[i - 1][j]
                    if added == 2:
                        break
            else:
                dp[i][j] += dp[i - 1][j]

    letters = [0 for _ in range(26)]
    for y in range(n):
        if dp[m - 1][y] != 0:
            for char in dp[0][y][0]:
                letters[ord(char) - 65] += dp[m - 1][y]

    result = (ceil(max(letters) / 2) - ceil(min(value for value in letters if value > 0) / 2))

    return result


print(dynamic_part_two(template))