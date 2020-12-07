def part1(input):
    for i, value in enumerate(input):
        for j in range(i + 1, len(input)):
            val_i, val_j = int(input[i]), int(input[j])
            if val_i + val_j == 2020:
                return val_i, val_j, val_i * val_j
    return None, None, None


def part2(input):
    for i, value in enumerate(input):
        for j in range(i + 1, len(input)):
            for k in range(j + 1, len(input)):
                val_i, val_j, val_k = int(input[i]), int(input[j]), int(input[k])
                if val_i + val_j + val_k == 2020:
                    return val_i, val_j, val_k, val_i * val_j * val_k
    return None, None, None


if __name__ == '__main__':
    with open('day1/input.txt') as input_file:
        inp = input_file.readlines()
        print(f'Part 1: {part1(inp)}')
        print(f'Part 2: {part2(inp)}')
