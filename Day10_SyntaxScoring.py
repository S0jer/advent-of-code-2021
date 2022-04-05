def error_syntax(A):
    illegal = [0 for _ in range(4)]
    for line in A:
        open = []
        for letter in line:
            if letter == '(':
                open.append('(')
            elif letter == '[':
                open.append('[')
            elif letter == '{':
                open.append('{')
            elif letter == '<':
                open.append('<')
            elif letter == ')' and open[len(open) - 1] == '(':
                open.pop(len(open) - 1)
            elif letter == ')' and open[len(open) - 1] != '(':
                illegal[0] += 1
                break
            elif letter == ']' and open[len(open) - 1] == '[':
                open.pop(len(open) - 1)
            elif letter == ']' and open[len(open) - 1] != '[':
                illegal[1] += 1
                break
            elif letter == '}' and open[len(open) - 1] == '{':
                open.pop(len(open) - 1)
            elif letter == '}' and open[len(open) - 1] != '{':
                illegal[2] += 1
                break
            elif letter == '>' and open[len(open) - 1] == '<':
                open.pop(len(open) - 1)
            elif letter == '>' and open[len(open) - 1] != '<':
                illegal[3] += 1
                break

    result = illegal[0] * 3 + illegal[1] * 57 + illegal[2] * 1197 + illegal[3] * 25137

    return result


def repair_syntax(A):
    illegal = [0 for _ in range(4)]
    repair_cost = []
    for line in A:
        open = []
        check = 0
        for letter in line:
            if letter == '(':
                open.append('(')
            elif letter == '[':
                open.append('[')
            elif letter == '{':
                open.append('{')
            elif letter == '<':
                open.append('<')
            elif letter == ')' and open[len(open) - 1] == '(':
                open.pop(len(open) - 1)
            elif letter == ')' and open[len(open) - 1] != '(':
                illegal[0] += 1
                check = 1
                break
            elif letter == ']' and open[len(open) - 1] == '[':
                open.pop(len(open) - 1)
            elif letter == ']' and open[len(open) - 1] != '[':
                illegal[1] += 1
                check = 1
                break
            elif letter == '}' and open[len(open) - 1] == '{':
                open.pop(len(open) - 1)
            elif letter == '}' and open[len(open) - 1] != '{':
                illegal[2] += 1
                check = 1
                break
            elif letter == '>' and open[len(open) - 1] == '<':
                open.pop(len(open) - 1)
            elif letter == '>' and open[len(open) - 1] != '<':
                illegal[3] += 1
                check = 1
                break
        if check == 0:
            repair_cost.append(count_cost(open))

    repair_cost.sort()
    if len(repair_cost) % 2 == 0:
        n = len(repair_cost) // 2
        result = (repair_cost[n] + repair_cost[n - 1]) / 2
    else:
        result = repair_cost[(len(repair_cost) - 1) // 2]


    return result

def count_cost(A):
    result = 0
    for i in range(len(A) - 1, -1, -1):
        result *= 5
        if A[i] == '(':
            result += 1
        elif A[i] == '[':
            result += 2
        elif A[i] == '{':
            result += 3
        elif A[i] == '<':
            result += 4

    return result


if __name__ == '__main__':
    A = []
    with open("data/day10ErrorSyntax.txt") as f:
        for line in f:
            A.append(str(line))

    B = ["[({(<(())[]>[[{[]{<()<>>",
         "[(()[<>])]({[<{<<[]>>(",
         "{([(<{}[<>[]}>{[]{[(<()>",
         "(((({<>}<{<{<>}{[]{[]{}",
         "[[<[([]))<([[{}[[()]]]",
         "[{[{({}]{}}([{[{{{}}([]",
         "{<[[]]>}<{[{[{[]{()[[[]",
         "[<(<(<(<{}))><([]([]()",
         "<{([([[(<>()){}]>(<<{{",
         "<{([{{}}[<[[[<>{}]]]>[]]"]

    print(error_syntax(A))
    print(repair_syntax(A))
