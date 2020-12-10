def part1(inp):
    adapters = sorted(inp, reverse=True)
    adapters = [adapters[0] + 3] + adapters
    prev = 0
    one = 0
    three = 0
    while len(adapters) > 0:
        curr = adapters.pop()
        if curr - prev == 1:
            one += 1
        elif curr - prev == 3:
            three += 1
        prev = curr

    return one * three


def part2(inp):
    adapters = sorted(inp)
    return part2_recursive(adapters, len(adapters) - 1)


def part2_recursive(adapters, index, memo=None):
    if memo is None:
        memo = {}

    if index == -1:
        return 1
    elif index in memo:
        return memo[index]

    count = 0
    curr = adapters[index]
    for i in range(index - 3, index):
        if i == -1 or 0 <= curr - adapters[i] <= 3:
            count += part2_recursive(adapters, i, memo)

    memo[index] = count
    return count


if __name__ == '__main__':
    with open('input.txt') as input_file:
        inp = [int(line.strip()) for line in input_file.readlines()]
        print(f'Part 1: {part1(inp)}')
        print(f'Part 2: {part2(inp)}')
