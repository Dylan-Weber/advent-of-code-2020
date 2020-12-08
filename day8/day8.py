def part1(inp):
    split = [line.split(' ') for line in inp]
    return run_program(split)[0]


def part2(inp):
    split = [line.split(' ') for line in inp]

    new_split = [line[:] for line in split]
    for index, line in enumerate(split):
        if line[0] == 'jmp':
            new_split[index][0] = 'nop'
        elif line[0] == 'nop':
            new_split[index][0] = 'jmp'

        acc, is_infinite = run_program(new_split)
        if not is_infinite:
            return acc

        new_split[index][0] = line[0]

    return None


def run_program(program):
    acc = 0
    seen = set()
    i = 0

    while i < len(program) and i not in seen:
        seen.add(i)
        if program[i][0] == 'acc':
            acc += int(program[i][1])
        elif program[i][0] == 'jmp':
            i += int(program[i][1]) - 1
        i += 1

    if i in seen:
        is_infinite = True
    else:
        is_infinite = False

    return acc, is_infinite


if __name__ == '__main__':
    with open('input.txt') as input_file:
        inp = [line.strip() for line in input_file.readlines()]
        print(f'Part 1: {part1(inp)}')
        print(f'Part 2: {part2(inp)}')
