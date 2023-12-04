def main():
    with open("input.txt") as f:
        lines = f.readlines()

    power_sum = 0

    for line in lines:
        game = line.split(":")[1]
        game = game.split(";")

        game_dict = {"red": 0, "green": 0, "blue": 0}

        for draw in game:
            draw = draw.split(",")
            draw = [d.strip() for d in draw]

            draw_dict = {}
            for d in draw:
                d = d.split(" ")
                draw_dict[d[1]] = int(d[0])

            for key in draw_dict.keys():
                if draw_dict[key] > game_dict[key]:
                    game_dict[key] = draw_dict[key]
        values = []
        for value in game_dict.values():
            values.append(value)
        power = values[0] * values[1] * values[2]
        power_sum += power

    print(power_sum)


if __name__ == "__main__":
    main()
