def part1(inp):
    count = 0
    curr = set()
    for line in inp:
        if line == '\n':
            count += len(curr)
            curr = set()
        curr |= set(line[:-1])
    count += len(curr)
    return count


def part2(inp):
    count = 0
    curr = None
    for line in inp:
        if line == '\n':
            count += len(curr)
            curr = None
        elif curr is None:
            curr = set(line[:-1])
        else:
            curr = curr.intersection(set(line[:-1]))
    count += len(curr)
    return count


if __name__ == '__main__':
    with open('input.txt') as input_file:
        inp = input_file.readlines()
        print(f'Part 1: {part1(inp)}')
        print(f'Part 2: {part2(inp)}')
