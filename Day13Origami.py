with open("day13FoldingTest.txt") as f:
    dots = []
    foldAlong = []
    for line in f:
        if 'fold' not in line and ',' in line:
            dots.append([int(x) for x in line.strip('\n').split(',')])
        elif 'fold' in line:
            foldAlong.append([x for x in line.strip('fold along\n\r').split('=')])
            foldAlong[-1][1] = int(foldAlong[-1][1])


def folding(foldInstrucion, dots):
    newDots = []
    if foldInstrucion[0] == 'x':
        border = foldInstrucion[1]
        for dot in dots:
            if dot[0] < border:
                if dot not in newDots:
                    newDots.append(dot)
            else:
                newDot = [border - (dot[0] - border), dot[1]]
                if newDot not in newDots:
                    newDots.append(newDot)
    elif foldInstrucion[0] == 'y':
        border = foldInstrucion[1]
        for dot in dots:
            if dot[1] < border:
                if dot not in newDots:
                    newDots.append(dot)
            else:
                newDot = [dot[0], border - (dot[1] - border)]
                if newDot not in newDots:
                    newDots.append(newDot)
    return newDots


cnt = 0
for foldInstrucion in foldAlong:
    dots = folding(foldInstrucion, dots)
    print(len(dots))
    cnt += 1


def display(dots):
    x_max = max([x for x, y in dots])
    y_max = max([y for x, y in dots])
    x_min = min([x for x, y in dots])
    y_min = min([y for x, y in dots])

    lines = []
    for y in range(y_min, y_max + 1):
        line = []
        for x in range(x_min, x_max + 1):
            if [x, y] in dots:
                line.append("x")
            else:
                line.append(" ")
        lines.append("".join(line))

    print("\n".join(lines))


display(dots)
