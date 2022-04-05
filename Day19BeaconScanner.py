from math import inf

n = 0
with open("data/day19BeaconTest.txt") as f:
    for line in f:
        if "scanner" in line:
            n += 1

with open("data/day19BeaconTest.txt") as f:
    scanners = [[] for _ in range(n)]
    idx = -1
    for line in f:
        if "scanner" in line:
            idx += 1
        elif "," in line:
            scanners[idx].append([int(x) for x in (line.strip("\n").split(","))])

relativeBy = [(1, 1, 1), (-1, -1, -1), (1, 1, -1), (1, -1, 1), (-1, 1, 1), (-1, -1, 1), (-1, 1, -1), (1, -1, -1)]

beaconsFromScannerZero = []
Known_positions = [None for _ in range(n)]
Known_positions[0] = (0, 0, 0)
used, done = [-1 for _ in range(n)], False
scannerAt, basicScanner = 0, 0
used[basicScanner] = 1
while not done:
    for j in range(n):
        if used[j] == -1:
            for r in relativeBy:
                found = False
                list_of_diff = [[inf, []]]

                for start in scanners[scannerAt]:
                    for positions in scanners[j]:
                        diff = [start[0] + r[0] * positions[0], start[1] + r[1] * positions[1],
                                start[2] + r[2] * positions[2]]
                        added = False
                        for id in range(len(list_of_diff)):
                            if list_of_diff[id][0] == diff:
                                print("DODAŁO : O ")
                                list_of_diff[id][1].append((start, positions))
                                added = True

                        if not added:
                            list_of_diff.append([diff, [(start, positions)]])

                for id in range(len(list_of_diff)):
                    if len(list_of_diff[id][1]) >= 12:
                        print(list_of_diff[id])
                        found = True
                        id_f = id
                        break
                print(scannerAt, j)
                if found:
                    scannerAt = j
                    used[j] = 1

    if sum(used) == n:
        done = True
