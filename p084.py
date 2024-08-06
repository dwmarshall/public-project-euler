from collections import deque, Counter
from generators import dice
from random import shuffle

SQUARES = 40

# named squares
BOARDWALK = 39
CHANCE = {7, 22, 36}
COMMUNITY_CHEST = {2, 17, 33}
GO = 0
GO_TO_JAIL = 30
ILLINOIS = 24
JAIL = 10
READING = 5
ST_CHARLES = 11

# Special Change
NEXT_RAILWAY = -1
NEXT_UTILITY = -2
GO_BACK_3 = -3

chance = deque(
    [None] * 6
    + [
        GO,
        JAIL,
        ST_CHARLES,
        ILLINOIS,
        BOARDWALK,
        READING,
        NEXT_RAILWAY,
        NEXT_RAILWAY,
        NEXT_UTILITY,
        GO_BACK_3,
    ]
)
shuffle(chance)
community_chest = deque([None] * 14 + [GO, JAIL])
shuffle(community_chest)

N = 1000000
D = dice.rolls(4, 4)

squares = Counter()

current_square = 0
doubles = 0

for _ in range(N):
    d1, d2 = next(D)
    doubles = doubles + 1 if d1 == d2 else 0
    if doubles == 3:
        current_square = JAIL
        doubles = 0
    else:
        current_square += d1 + d2
        current_square %= SQUARES
        if current_square == GO_TO_JAIL:
            current_square = JAIL
        elif current_square in COMMUNITY_CHEST:
            cc_card = community_chest[0]
            community_chest.rotate(-1)
            if cc_card is not None:
                current_square = cc_card
        elif current_square in CHANCE:
            ch_card = chance[0]
            chance.rotate(-1)
            if ch_card is not None and ch_card >= 0:
                current_square = ch_card
            elif ch_card == GO_BACK_3:
                current_square -= 3
            elif ch_card == NEXT_RAILWAY:
                if current_square == 7:
                    current_square = 15
                elif current_square == 22:
                    current_square = 25
                else:
                    current_square = 5
            elif ch_card == NEXT_UTILITY:
                if current_square == 22:
                    current_square = 28
                else:
                    current_square = 12

    squares[current_square] += 1

for square, hits in squares.most_common(3):
    print(f"{square}: {hits * 100 / N}%")

modal = [f"{x[0]:02d}" for x in squares.most_common(3)]
print("".join(modal))
