def part1(input, slope):
    dy, dx = slope
    x = y = 0
    count = 0
    while y < len(input):
        row = input[y]
        if row[x] == '#':
            count += 1
        y += dy
        x += dx
        x %= len(row) - 1
    return count


def part2(input):
    return part1(input, (1, 1)) * part1(input, (1, 3)) * \
           part1(input, (1, 5)) * part1(input, (1, 7)) * part1(input, (2, 1))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('input.txt') as input_file:
        inp = input_file.readlines()
        print(f'Part 1: {part1(inp, (1, 3))}')
        print(f'Part 2: {part2(inp)}')
