def part1(inp):
    curr = None
    next = inp
    while next != curr:
        curr = next
        next = [[None] * len(curr[0]) for i in range(len(curr))]
        for y, line in enumerate(curr):
            for x, seat in enumerate(line):
                if seat == '.':
                    next[y][x] = '.'
                    continue
                occupied_count = occupied_points(curr, ((x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1),
                                           (x, y + 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)))

                if occupied_count == 0:
                    next[y][x] = '#'
                elif occupied_count >= 4:
                    next[y][x] = 'L'
                else:
                    next[y][x] = seat

    return occupied_in_seating(next)


def occupied_points(curr, points):
    count = 0
    for p in points:
        x, y = p
        if 0 <= y < len(curr) and 0 <= x < len(curr[0]) and curr[y][x] == '#':
            count += 1
    return count


def occupied_in_seating(seating):
    count = 0
    for line in seating:
        for seat in line:
            if seat == '#':
                count += 1
    return count


def part2(inp):
    curr = None
    next = inp
    while next != curr:
        curr = next
        next = [[None] * len(curr[0]) for i in range(len(curr))]
        for y, line in enumerate(curr):
            for x, seat in enumerate(line):
                if seat == '.':
                    next[y][x] = '.'
                    continue
                occupied_count = occupied_sight(curr, (x, y))

                if occupied_count == 0:
                    next[y][x] = '#'
                elif occupied_count >= 5:
                    next[y][x] = 'L'
                else:
                    next[y][x] = seat

    return occupied_in_seating(next)


def occupied_sight(curr, point):
    c = 0
    directions = {(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1), (-1, 1)}
    # More gross hardcoding
    # Sorry to the one person person that maybe reads this,
    # I was trying to get a top score and couldn't think of a neat way
    i = 1
    x, y = point
    while len(directions) > 0:
        new_directions = set()
        for dx, dy in directions:
            new_x = x + i * dx
            new_y = y + i * dy
            if 0 <= new_y < len(curr) and 0 <= new_x < len(curr[0]):
                if curr[new_y][new_x] == '#':
                    c += 1
                elif curr[new_y][new_x] != 'L':
                    new_directions.add((dx, dy))

        directions = new_directions

        i += 1
    return c


if __name__ == '__main__':
    with open('input.txt') as input_file:
        inp = [list(line                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       .strip()) for line in input_file.readlines()]
        print(f'Part 1: {part1(inp)}')
        print(f'Part 2: {part2(inp)}')
