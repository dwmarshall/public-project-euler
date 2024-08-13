from itertools import combinations

required_digits = list(range(10))

required_pairs = [(0, 1), (0, 4), (2, 5), (1, 8)]
digits_requiring_6_or_9 = [0, 1, 3, 4]

valid_arrangements = set()

for first_die in combinations(required_digits, 6):
    for second_die in combinations(required_digits, 6):
        valid_arrangement = True
        for first_digit, second_digit in required_pairs:
            if first_digit in first_die and second_digit in second_die:
                continue
            if first_digit in second_die and second_digit in first_die:
                continue
            valid_arrangement = False
            break
        for d in digits_requiring_6_or_9:
            if d in first_die and (6 in second_die or 9 in second_die):
                continue
            if d in second_die and (6 in first_die or 9 in first_die):
                continue
            valid_arrangement = False
            break

        if valid_arrangement:
            sorted_first_die = tuple(sorted(first_die))
            sorted_second_die = tuple(sorted(second_die))
            sorted_tuples = tuple(sorted([sorted_first_die, sorted_second_die]))
            print(f"{sorted_tuples} qualify!")
            valid_arrangements.add(sorted_tuples)


print(len(valid_arrangements))
