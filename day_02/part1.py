cubes = {"red": 12, "green": 13, "blue": 14}


def main():
    with open("input.txt") as f:
        lines = f.readlines()

    valid_sum = 0
    for line in lines:
        valid_game = True
        id = line.split(":")[0]
        id = int(id.split(" ")[1])

        game = line.split(":")[1]
        game = game.split(";")

        for draw in game:
            draw = draw.split(",")
            draw = [d.strip() for d in draw]

            draw_dict = {}
            for d in draw:
                d = d.split(" ")
                draw_dict[d[1]] = int(d[0])

            for key in draw_dict.keys():
                if draw_dict[key] > cubes[key]:
                    valid_game = False
                    break

        if valid_game:
            valid_sum += id

    print(valid_sum)


if __name__ == "__main__":
    main()
