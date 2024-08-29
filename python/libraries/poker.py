from collections import Counter
from dataclasses import dataclass

CARDS = {x: 2**i for i, x in enumerate("23456789TJQKA")}

HIGH_CARD = 0
ONE_PAIR = 1
TWO_PAIRS = 2
TRIPS = 3
STRAIGHT = 4
FLUSH = 5
FULL_HOUSE = 6
QUADS = 7
STRAIGHT_FLUSH = 8

STRAIGHTS = {sum(1 << x for x in range(y, y + 5)) for y in range(9)}
WHEEL = (1 << 12) + sum(1 << x for x in range(4))
STRAIGHTS.add(WHEEL)


@dataclass(order=True)
class PokerHand:

    hand_type: int = 0
    quad_card: int = 0
    trip_card: int = 0
    pair_cards: int = 0
    high_cards: int = 0

    def __init__(self, cards: str):

        ranks = Counter()
        suits = Counter()
        for rank, suit in cards.split(" "):
            ranks[rank] += 1
            suits[suit] += 1

        pairs = [rank for rank, c in ranks.items() if c == 2]
        trips = [rank for rank, c in ranks.items() if c == 3]
        quads = [rank for rank, c in ranks.items() if c == 4]

        if quads:
            self.hand_type = QUADS
            self.quad_card = CARDS[quads[0]]
            del ranks[quads[0]]
        elif trips and pairs:
            self.hand_type = FULL_HOUSE
            self.trip_card = CARDS[trips[0]]
            self.pair_cards = CARDS[pairs[0]]
            del ranks[trips[0]], ranks[pairs[0]]
        elif trips:
            self.hand_type = TRIPS
            self.trip_card = CARDS[trips[0]]
            del ranks[trips[0]]
        elif len(pairs) == 2:
            self.hand_type = TWO_PAIRS
            self.pair_cards = CARDS[pairs[0]] + CARDS[pairs[1]]
            del ranks[pairs[0]], ranks[pairs[1]]
        elif len(pairs) == 1:
            self.hand_type = ONE_PAIR
            self.pair_cards = CARDS[pairs[0]]
            del ranks[pairs[0]]
        else:
            self.hand_type = HIGH_CARD

        for r in ranks.keys():
            self.high_cards += CARDS[r]

        is_flush = suits.total() == 5 and len(suits) == 1
        is_straight = self.high_cards in STRAIGHTS
        if is_flush and is_straight:
            self.hand_type = STRAIGHT_FLUSH
        elif is_flush:
            self.hand_type = FLUSH
        elif is_straight:
            self.hand_type = STRAIGHT
