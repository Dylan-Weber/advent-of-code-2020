required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}


def part1(input):
    valid = 0
    for d in input:
        if len(required_fields.intersection(d.keys())) == len(required_fields):
            valid += 1
    return valid


def part2(input):
    valid = 0
    for d in input:
        try:
            # I'm sorry to anyone who has to read this mess. I promise I wouldn't do this in production code.
            # Regex might have been a better idea.
            if len(required_fields.intersection(d.keys())) != len(required_fields) \
                    or not (len(d['byr']) == 4 and 1920 <= int(d['byr']) <= 2002) \
                    or not (len(d['iyr']) == 4 and 2010 <= int(d['iyr']) <= 2020) \
                    or not (len(d['eyr']) == 4 and 2020 <= int(d['eyr']) <= 2030) \
                    or not check_height(d['hgt']) \
                    or not (len(d['hcl']) == 7
                            and d['hcl'][0] == '#' and all(letter in '0123456789abcdef' for letter in d['hcl'][1:])) \
                    or d['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] \
                    or not (len(d['pid']) == 9 and all(letter in '0123456789' for letter in d['pid'])):
                continue
        except ValueError as e:
            continue
        valid += 1
    return valid


def check_height(hgt):
    for i, ch in enumerate(hgt):
        if ch not in '0123456789':
            break

    if hgt[i:] not in ['cm', 'in']:
        return False
    elif hgt[i:] == 'cm' and not (150 <= int(hgt[:i]) <= 193):
        return False
    elif hgt[i:] == 'in' and not (59 <= int(hgt[:i]) <= 76):
        return False
    return True


def make_dicts(lines):
    dicts = []
    d = {}
    for line in lines:
        if line == '\n':
            dicts.append(d)
            d = {}
            continue
        for pair in line.split(' '):
            trimmed = pair.strip()
            key, val = trimmed.split(':')
            d[key] = val
    dicts.append(d)
    return dicts


if __name__ == '__main__':
    with open('input.txt') as input_file:
        inp = make_dicts(input_file.readlines())
        print(f'Part 1: {part1(inp)}')
        print(f'Part 2: {part2(inp)}')
