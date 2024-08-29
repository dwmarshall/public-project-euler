from libraries import poker


def test_init():
    h = poker.PokerHand("2H")
    assert h.hand_type == poker.HIGH_CARD
    assert h.high_cards == 1

    h = poker.PokerHand("2H 3C 4S")
    assert h.hand_type == poker.HIGH_CARD
    assert h.high_cards == (1 << 0) + (1 << 1) + (1 << 2)

    h = poker.PokerHand("AS")
    assert h.hand_type == poker.HIGH_CARD
    assert h.high_cards == 1 << 12


def test_pair():
    h = poker.PokerHand("2H 2C")
    assert h.hand_type == poker.ONE_PAIR
    assert h.pair_cards == 1
    assert h.high_cards == 0

    h = poker.PokerHand("2H 2C 5S")
    assert h.hand_type == poker.ONE_PAIR
    assert h.pair_cards == 1
    assert h.high_cards == 1 << 3


def test_two_pair():
    h = poker.PokerHand("2H 2C 5S 5C 6S")
    assert h.hand_type == poker.TWO_PAIRS
    assert h.pair_cards == (1 << 0) + (1 << 3)
    assert h.high_cards == 1 << 4


def test_trips():
    h = poker.PokerHand("5H 5S 5C 2D 3C")
    assert h.hand_type == poker.TRIPS
    assert h.trip_card == 1 << 3
    assert h.high_cards == (1 << 0) + (1 << 1)


def test_straight():
    test_straights = {
        0: "2C 3H 4D 5S 6S",
        1: "3C 4H 5D 6S 7S",
        2: "4C 5H 6D 7S 8S",
        3: "5C 6H 7D 8S 9S",
        4: "6C 7H 8D 9S TS",
        5: "7C 8H 9D TS JS",
        6: "8C 9H TD JS QS",
        7: "9C TH JD QS KS",
        8: "TC JH QD KS AS",
    }
    for rank, hand in test_straights.items():
        h = poker.PokerHand(hand)
        assert h.hand_type == poker.STRAIGHT
        assert h.high_cards == sum(1 << x for x in range(rank, rank + 5))


def test_wheel():
    h = poker.PokerHand("AC 2D 3S 4D 5C")
    assert h.hand_type == poker.STRAIGHT
    assert h.high_cards == sum(1 << x for x in range(4)) + (1 << 12)


def test_flush():
    h = poker.PokerHand("2S 4S 6S 8S TS")
    assert h.hand_type == poker.FLUSH
    assert h.high_cards == sum(1 << x for x in range(0, 9, 2))


def test_full_house():
    h = poker.PokerHand("5H 5S 5C 2D 2C")
    assert h.hand_type == poker.FULL_HOUSE
    assert h.trip_card == 1 << 3
    assert h.pair_cards == 1 << 0


def test_quads():
    h = poker.PokerHand("5C 5D 5H 5S 3H")
    assert h.hand_type == poker.QUADS
    assert h.quad_card == 1 << 3
    assert h.high_cards == 1 << 1


def test_straight_flush():
    h = poker.PokerHand("2S 3S 4S 5S 6S")
    assert h.hand_type == poker.STRAIGHT_FLUSH
    assert h.high_cards == sum(1 << x for x in range(5))


def test_hands():
    hands = [
        ["5H 5C 6S 7S KD 2C 3S 8S 8D TD", 1],
        ["5D 8C 9S JS AC 2C 5C 7D 8S QH", 0],
        ["2D 9C AS AH AC 3D 6D 7D TD QD", 1],
        ["4D 6S 9H QH QC 3D 6D 7H QD QS", 0],
        ["2H 2D 4C 4D 4S 3C 3D 3S 9S 9D", 0],
    ]
    for s, winner in hands:
        h1 = poker.PokerHand(s[:14])
        h2 = poker.PokerHand(s[15:])
        assert winner == 0 if h1 > h2 else 1
