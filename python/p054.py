from libraries.poker import PokerHand

winners = 0
with open("../data/0054_poker.txt") as f:
    for s in f:
        h1 = PokerHand(s[:14])
        h2 = PokerHand(s[15:-1])
        if h1 > h2:
            winners += 1

print(winners)
