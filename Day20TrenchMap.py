import sys
import heapq
import itertools
import re
import ast
from collections import defaultdict, Counter, deque

with open("data/day20MapTest.txt") as f:
    code = ""
    for line in f:
        for element in line:
            if element == "." or element == "#":
                code += element
        if "." not in line:
            break
    TrenchMap = []
    for line in f:
        row = ""
        for element in line:
            if element == "." or element == "#":
                row += element
        TrenchMap.append(row)

print(len(TrenchMap), len(TrenchMap[0]))


def extend(TrenchMap):
    # for i in range(len(TrenchMap)):
    #     TrenchMap[i] = "." + TrenchMap[i] + "."
    #     TrenchMap[i] = "." + TrenchMap[i] + "."
    n = len(TrenchMap[0])

    line = ""
    for i in range(n):
        line += "."

    new_map = []
    for i in range(n):
        new_map.append(line)

    # TrenchMap.insert(0, line)
    # TrenchMap.append(line)

    return TrenchMap, new_map


def cut(new_map):
    while "#" not in new_map[0]:
        new_map.pop(0)

    while "#" not in new_map[len(new_map) - 1]:
        new_map.pop(len(new_map) - 1)

    done = False
    while not done:
        cnt = 0
        for i in range(len(new_map)):
            if new_map[i][0] == "#":
                cnt += 1
                break
        if cnt == 0:
            for i in range(len(new_map)):
                new_map[i] = new_map[i][1:]
        else:
            done = True

    done = False
    while not done:
        cnt = 0
        for i in range(len(new_map)):
            if new_map[i][len(new_map[i]) - 1] == "#":
                cnt += 1
                break
        if cnt == 0:
            for i in range(len(new_map)):
                new_map[i] = new_map[i][:len(new_map[i]) - 1]
        else:
            done = True


def enhancement_image(TrenchMap, code):
    TrenchMap, new_map = extend(TrenchMap)

    for i in range(n):
        for j in range(m):
            binary_string = ""
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if x < 0 or x >= n or y < 0 or y >= m:
                        binary_string += "0"
                    elif TrenchMap[x][y] == ".":
                        binary_string += "0"
                    else:
                        binary_string += "1"

            idx = int(binary_string, 2)

            if code[idx] == "#":
                new_map[i] = new_map[i][:j] + "#" + new_map[i][j + 1:]

    # cut(new_map)

    lit = 0
    for line in new_map:
        for element in line:
            if element == "#":
                lit += 1

    for el in TrenchMap:
        print(el)

    print()

    for line in new_map:
        print(line)

    return new_map, lit


cnt = 0
n, m = len(TrenchMap), len(TrenchMap[0])
TrenchMap, lit= enhancement_image(TrenchMap, code)
print(lit)
TrenchMap, lit = enhancement_image(TrenchMap, code)
print(lit)

# ------------------------------------------------------------------------------------------------------


infile = sys.argv[1] if len(sys.argv) > 1 else 'data/day20MapTest.txt'
data = open(infile).read().strip()

rule, start = data.split('\n\n')
rule = rule.strip()
assert len(rule) == 512
# print(rule[0], rule[511])

G = set()
for r, line in enumerate(start.strip().split('\n')):
    for c, x in enumerate(line.strip()):
        if x == '#':
            G.add((r, c))


# on=true means G says what pixels are on (all the rest are off).
# on=false means G says what pixels are *off* (all the rest are on)
def step(G, on):
    G2 = set()
    rlo = min([r for r, c in G])
    rhi = max([r for r, c in G])
    clo = min([c for r, c in G])
    chi = max([c for r, c in G])
    print(rlo, rhi, clo, chi)
    for r in range(rlo - 5, rhi + 10):
        for c in range(clo - 5, chi + 10):
            rc_str = 0
            bit = 8
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if ((r + dr, c + dc) in G) == on:
                        rc_str += 2 ** bit
                    bit -= 1
            assert 0 <= rc_str < 512
            if (rule[rc_str] == '#') != on:
                G2.add((r, c))
    return G2


def show(G):
    rlo = min([r for r, c in G])
    rhi = max([r for r, c in G])
    clo = min([c for r, c in G])
    chi = max([c for r, c in G])
    for r in range(rlo - 5, rhi + 5):
        row = ''
        for c in range(clo - 5, chi + 5):
            if (r, c) in G:
                row += '#'
            else:
                row += ' '
        print(row)


for t in range(50):
    if t == 2:
        print(len(G))
    G = step(G, t % 2 == 0)
print(len(G))
