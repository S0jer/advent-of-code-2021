def bingo_subsystem(drawn, cards):
    found, i = False, 0
    while found == False or i >= len(drawn):
        number = drawn[i]
        for card in cards:
            for j in range(len(card)):
                if card[j] == number:
                    card[j] = 100
        j = 0
        for idx in range(len(cards)):
            if isWinner(cards[idx - j]):
                if len(cards) == 1:
                    sums = 0
                    for x in cards[idx - j]:
                        if x != 100:
                            sums += x
                    result = sums * number

                    found = True
                cards.pop(idx - j)
                j += 1

        i += 1

    return result


def isWinner(card):
    for start in range(0, 21, 5):
        if card[start] + card[start + 1] + card[start + 2] + card[start + 3] + card[start + 4] == 500:
            return True

    for start in range(5):
        if card[start] + card[start + 5] + card[start + 10] + card[start + 15] + card[start + 20] == 500:
            return True

    return False


if __name__ == '__main__':
    with open("data/bingoTest.txt") as f:
        drawn = [int(x) for x in f.readline().strip('\n').split(',')]
        cards = []
        while f.readline():
            card = []
            for i in range(5):
                card.extend([int(x) for x in f.readline().strip('\n').split(' ') if x != ''])
            cards.append(card)

    print(bingo_subsystem(drawn, cards))
