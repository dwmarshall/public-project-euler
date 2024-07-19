D = 1001

first_diag = [n * n for n in range(1, D + 1, 2)]
second_diag = [first_diag[i] - 2 * i for i in range(len(first_diag))]
third_diag = [first_diag[i] - 4 * i for i in range(len(first_diag))]
fourth_diag = [first_diag[i] - 6 * i for i in range(len(first_diag))]


print(
    sum(first_diag) + sum(second_diag[1:]) + sum(third_diag[1:]) + sum(fourth_diag[1:])
)
