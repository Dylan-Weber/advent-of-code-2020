def part1(inp):
    graph = {}
    for line in inp:
        name, contains = line.split(' bags contain ')
        contain_list = [bag[2:bag.rfind('bag')].strip() for bag in contains.split(', ')]
        graph[name] = contain_list

    count = 0
    for bag_type in graph:
        if contains_gold(graph, bag_type):
            count += 1
    return count


def contains_gold(contain_dict, bag_type, seen=None):
    if seen is None:
        seen = set()
    elif bag_type in seen:
        return False

    if bag_type not in contain_dict:
        return False
    if 'shiny gold' in contain_dict[bag_type]:
        return True

    for type in contain_dict[bag_type]:
        if contains_gold(contain_dict, type, seen | {bag_type}):
            return True
    return False


def part2(inp):
    graph_with_counts = {}
    for line in inp:
        name, contains = line.split(' bags contain ')
        if contains == 'no other bags.':
            contain_list = []
        else:
            contain_list = [(int(bag[0]), bag[2:bag.rfind('bag')].strip()) for bag in contains.split(', ')]
        graph_with_counts[name] = contain_list

    count = total_count(graph_with_counts, 'shiny gold')
    return count


def total_count(contain_dict, bag_type):
    count = 0
    for type in contain_dict[bag_type]:
        result = total_count(contain_dict, type[1])
        count += type[0] * result + type[0]
    return count


if __name__ == '__main__':
    with open('input.txt') as input_file:
        inp = [line.strip() for line in input_file.readlines()]
        print(f'Part 1: {part1(inp)}')
        print(f'Part 2: {part2(inp)}')