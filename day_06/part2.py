def read_input():
    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
        times = lines[0]
        distances = lines[1]

    return times, distances


def main():
    times, distances = read_input()
    times = times.split(":")[1].split(" ")
    distances = distances.split(":")[1].split(" ")

    # combine
    time = int("".join(times))
    distance = int("".join(distances))

    wins = 0
    possible_holds = [i for i in range(time + 1)]
    possible_distances = [x * (time - x) for x in possible_holds]

    for p in possible_distances:
        if p > distance:
            wins += 1

    print(wins)


if __name__ == "__main__":
    main()
