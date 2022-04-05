from queue import PriorityQueue

area = [[236, -78], [262, -58]]

start = [0, 0]
position = []
max_heights = []


def move(position, vector):
    position[0] += vector[0]
    position[1] += vector[1]

    if vector[0] > 0:
        vector[0] -= 1
    vector[1] -= 1

    return position, vector


def will_hit(position, vector):
    global max_heights
    start_vector = vector
    height = position[1]
    while not not_hit(position, vector):
        position, vector = move(position, vector)
        height = max(height, position[1])
        if in_area(position):
            max_heights.append(start_vector)
            return True, height

    return False, None


def in_area(position):
    return (area[0][0] <= position[0] <= area[1][0] and area[0][1] <= position[1] <= area[1][1])


def not_hit(position, vector):
    if vector[0] > 0 and position[0] > area[1][0]:
        return True
    if vector[0] < 0 and position[0] < area[0][0]:
        return True
    if vector[1] < 0 and position[1] < area[0][1]:
        return True
    return False


max_yv, y = area[0][1], abs(area[0][1])
max_xv = abs(area[1][0])
max_height = 0
while y >= max_yv:
    done = False
    for x in range(-1 * area[0][0], area[1][0] + 1):
        work, height = will_hit([0, 0], [x, y])
        if work:
            max_height = max(max_height, height)
    y -= 1

print(len(max_heights), max_height)
