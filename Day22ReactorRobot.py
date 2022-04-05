from math import inf

import itertools

cubes = []
with open("day22CubeTest.txt") as f:
    cnt = 0
    minimum, maximum = inf, - inf
    for line in f:
        cubes.append(["on" if "on" in line else "off", []])
        id = 0
        for diagonal in line.strip('on off x=\n').split(','):
            diagonal = diagonal.strip('y=').strip('z=').split('..')
            cubes[cnt][1].append([int(x) for x in range(int(diagonal[0]), int(diagonal[1]) + 1)])
            if len(cubes[cnt][1][id]) > 0:
                minimum, maximum = min(min(cubes[cnt][1][id]), minimum), max(max(cubes[cnt][1][id]), maximum)
            id += 1
        cnt += 1

minimum = abs(minimum)

region = [[[0 for _ in range(minimum + maximum + 1)] for _ in range(minimum + maximum + 1)] for _ in
          range(minimum + maximum + 1)]

add = minimum
for cube in cubes:
    for x, y, z in itertools.product(cube[1][0], cube[1][1], cube[1][2]):
        if cube[0] == 'on':
            region[x + add][y + add][z + add] = 1
        elif cube[0] == 'off':
            region[x + add][y + add][z + add] = 0

result = 0
for x in range(minimum + maximum + 1):
    for y in range(minimum + maximum + 1):
        result += sum(region[x][y])

print(result)
