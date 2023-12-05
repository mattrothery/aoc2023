def read_cards(file_name):
    with open(file_name, "r") as f:
        return [line.strip() for line in f.readlines()]


def main():
    cards = read_cards("input.txt")

    won_card_counts = {}
    for i in range(len(cards)):
        won_card_counts[i + 1] = 1

    for i, card in enumerate(cards):
        i = i + 1

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

        # each match wins you the next n cards, eg. if you are on card 1 and get 3 matches, you get a copy of cards 2, 3, and 4
        # if you are on card 2 and get 3 matches, you get a copy of cards 3, 4, and 5, twice because you already have a copy of card 2

        won_cards = [x for x in range(i + 1, i + len(matches) + 1)]

        for won_card in won_cards:
            if won_card not in won_card_counts:
                won_card_counts[won_card] = 1
            else:
                won_card_counts[won_card] += 1 * won_card_counts[i]

    print(sum(won_card_counts.values()))


if __name__ == "__main__":
    main()
