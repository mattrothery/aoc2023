import math


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

    times = [int(t) for t in times if t != ""]
    distances = [int(d) for d in distances if d != ""]

    ways_to_win = []
    for i, time in enumerate(times):
        wins = 0
        possible_holds = [i for i in range(time + 1)]
        possible_distances = [x * (time - x) for x in possible_holds]

        for p in possible_distances:
            if p > distances[i]:
                wins += 1

        ways_to_win.append(wins)

    print(math.prod(ways_to_win))


if __name__ == "__main__":
    main()
