def read_schematic(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def locate_symbols(schematic):
    symbols = {}
    for y, line in enumerate(schematic):
        for x, char in enumerate(line):
            if not char.isalnum() and char != ".":
                symbols[(x, y)] = char

    return symbols


def get_whole_number(schematic, x, y):
    # from x, y, go left and right until you hit a non-digit
    start, end = x, x
    while start >= 0 and schematic[y][start].isdigit():
        start -= 1
    while end < len(schematic[y]) and schematic[y][end].isdigit():
        end += 1

    return int(schematic[y][start + 1 : end])


def get_adjacent(schematic, x, y):
    adjacent = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            if schematic[y + j][x + i].isdigit():
                adjacent.append(get_whole_number(schematic, x + i, y + j))
    return set(adjacent)


def main():
    engine = read_schematic("input.txt")
    symbols = locate_symbols(engine)
    # print(symbols)

    valid_sum = 0
    for key in symbols.keys():
        adjacent = get_adjacent(engine, key[0], key[1])
        # print(f'line: {key[1]+1}, col: {key[0]+1}, adjacents: {adjacent}')
        valid_sum += sum(adjacent)

    print(valid_sum)


if __name__ == "__main__":
    main()
