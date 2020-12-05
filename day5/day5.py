def part1(input):
    max_id = 0
    for seat in input:
        max_id = max(max_id, id_from_string(seat))
    return max_id


def id_from_string(string):
    row_range = (0, 128)
    col_range = (0, 8)
    for letter in string:
        if letter == 'F':
            row_range = (row_range[0], (row_range[0] + row_range[1]) // 2)
        elif letter == 'B':
            row_range = ((row_range[0] + row_range[1]) // 2, row_range[1])
        elif letter == 'L':
            col_range = (col_range[0], (col_range[0] + col_range[1]) // 2)
        elif letter == 'R':
            col_range = ((col_range[0] + col_range[1]) // 2, col_range[1])

    return seat_id(col_range[0], row_range[0])


def seat_id(col, row):
    return row * 8 + col


def part2(input):
    all_ids = sorted(id_from_string(string) for string in input)
    for i, id in enumerate(all_ids):
        if i < len(all_ids) - 1 and id != all_ids[i + 1] - 1:
            return id + 1
    return None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('input.txt') as input_file:
        inp = input_file.readlines()
        print(f'Part 1: {part1(inp)}')
        print(f'Part 2: {part2(inp)}')
