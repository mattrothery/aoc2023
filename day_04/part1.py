def read_cards(file_name):
    with open(file_name, "r") as f:
        return [line.strip() for line in f.readlines()]


def main():
    cards = read_cards("input.txt")

    total = 0

    for card in cards:
        winning_card = card.split("|")[0]
        winning_card = winning_card.split(":")[1]
        winning_card = winning_card.strip()
        winning_card = winning_card.split(" ")

        winning_card = [x for x in winning_card if x != ""]
        winning_card = set([int(x) for x in winning_card])

        draw = card.split("|")[1]
        draw = draw.strip()
        draw = draw.split(" ")
        draw = [x for x in draw if x != ""]
        draw = set([int(x) for x in draw])

        matches = winning_card.intersection(draw)

        card_score = 0
        # for the first match, add 1. for each match after, double the score
        for i, match in enumerate(matches):
            if i == 0:
                card_score += 1
            else:
                card_score *= 2

        total += card_score

    print(total)


if __name__ == "__main__":
    main()
