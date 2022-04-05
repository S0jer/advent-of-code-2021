def paths():
    global solutions
    if path[-1] != 'end':
        for nextMove in graph[path[-1]]:
            if nextMove.upper() == nextMove or nextMove not in path:
                path.append(nextMove)
                paths()
                path.pop()

    else:
        solutions.append(path.copy())


def pathsSmallTwice():
    global solution
    if path2[-1] != 'end':
        for nextMove in graph[path2[-1]]:
            if nextMove != 'start' and smallTwice(path2) and (
                    nextMove.upper() == nextMove or path2.count(nextMove) < 2):
                path2.append(nextMove)
                pathsSmallTwice()
                path2.pop()

    elif smallTwice(path2):
        solution += 1


def smallTwice(path):
    smallOnly = [x for x in path if x.upper() != x]
    return len(smallOnly) - len(set(smallOnly)) <= 1


graph = dict()
A = []
for line in open("day12CaveTest.txt"):
    A = [str(x) for x in line.strip('\n\r').split('-')]

    if graph.get(A[0], "FirstTime") == "FirstTime":
        graph[A[0]] = []
    if graph.get(A[1], "FirstTime") == "FirstTime":
        graph[A[1]] = []
    graph[A[0]].append(A[1])
    graph[A[1]].append(A[0])

solutions, solution = [], 0
path = ["start"]
path2 = ["start"]
print(graph)

paths()
pathsSmallTwice()
print(len(solutions))
print(solution)
