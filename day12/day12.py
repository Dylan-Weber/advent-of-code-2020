from math import sin, cos, pi

directions = {'E': (1, 0), 'W': (-1, 0), 'S': (0, -1), 'N': (0, 1)}
rotation_order = ['E', 'S', 'W', 'N']


def part1(inp):
    rotation = 0
    x, y = 0, 0
    for line in inp:
        direction = line[0]
        distance = int(line[1:])
        if direction == 'R':
            rotation += distance // 90
        elif direction == 'L':
            rotation -= distance // 90
        else:
            if direction == 'F':
                direction_to_move = rotation_order[rotation]
            else:
                direction_to_move = direction
            dx, dy = directions[direction_to_move]

            x += distance * dx
            y += distance * dy

        rotation %= len(rotation_order)

    return abs(x) + abs(y)


def part2(inp):
    way_x, way_y = 10, 1
    x, y = 0, 0
    for line in inp:
        direction = line[0]
        distance = int(line[1:])
        if direction in ['R', 'L']:
            way_x, way_y = rotate_waypoint(way_x, way_y, direction, distance)
        elif direction == 'F':
            x += way_x * distance
            y += way_y * distance
        else:
            dx, dy = directions[direction]
            way_x += distance * dx
            way_y += distance * dy

    return abs(x) + abs(y)


def rotate_waypoint(way_x, way_y, direction, degrees):
    radians = degrees * pi / 180
    if direction == 'R':
        true_rotation = 2 * pi - radians
    elif direction == 'L':
        true_rotation = radians

    new_way_x = round(way_x * cos(true_rotation) - way_y * sin(true_rotation))
    new_way_y = round(way_x * sin(true_rotation) + way_y * cos(true_rotation))
    return new_way_x, new_way_y


if __name__ == '__main__':
    with open('input.txt') as input_file:
        inp = [line.strip() for line in input_file.readlines()]
        print(f'Part 1: {part1(inp)}')
        print(f'Part 2: {part2(inp)}')
