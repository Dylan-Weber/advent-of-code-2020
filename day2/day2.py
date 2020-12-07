def part1(input):
    valid = 0
    for start, finish, letter, password in input:
        if start <= password.count(letter) <= finish:
            valid += 1
    return valid

def part2(input):
    valid = 0
    for start, finish, letter, password in input:
        if (password[start - 1] == letter) != (password[finish - 1] == letter):
            valid += 1
    return valid

def clean_line(line):
    trimmed = line.strip()
    policy, password = trimmed.split(':')
    ranges, letter = policy.split(' ')
    start, finish = ranges.split('-')
    return int(start), int(finish), letter, password.strip()

if __name__ == '__main__':
    with open('input.txt') as input_file:
        inp = [clean_line(line) for line in input_file]
        print(inp)
        print(f'Part 1: {part1(inp)}')
        print(f'Part 2: {part2(inp)}')
