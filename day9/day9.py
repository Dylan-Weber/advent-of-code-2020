preamble_length = 25


def part1(inp):
    for i, val in enumerate(inp):
        if i >= preamble_length and not is_sum(i, inp):
            return val


def is_sum(index, vals):
    start_index = index - preamble_length
    for i, v1 in enumerate(vals[start_index:index]):
        for v2 in vals[start_index + 1:index]:
            if v1 + v2 == vals[index]:
                return True
    return False


def part2(inp):
    # Definitely not the fastest algorithm, but probably the fastest to type up
    result = part1(inp)
    for i, val in enumerate(inp):
        for j in range(i + 1, len(inp)):
            sub_inp = inp[i:j + 1]
            if sum(sub_inp) == result:
                return min(sub_inp) + max(sub_inp)


if __name__ == '__main__':
    with open('input.txt') as input_file:
        inp = [int(line.strip()) for line in input_file.readlines()]
        print(f'Part 1: {part1(inp)}')
        print(f'Part 2: {part2(inp)}')
