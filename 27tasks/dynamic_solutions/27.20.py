"""
Рассматриваются все пары различных элементов последовательности,
находящихся на расстоянии кратном 5
(разница в индексах элементов пары должна быть кратна 5,
порядок элементов в паре неважен).
Необходимо определить минимальную сумму пары, кратную 107.
"""
with open('27A.txt') as f:
    n = int(f.readline())
    min_sum = 20 ** 5 + 1
    mods = [[20 ** 5 + 1] * 107 for _ in range(5)]

    for i in range(n):
        x = int(f.readline())
        mod = 0 if x % 107 == 0 else 107 - x % 107
        if mods[i % 5][mod] != 20 ** 5 + 1:
            min_sum = min(min_sum, mods[i % 5][mod] + x)

        mods[i % 5][x % 107] = min(mods[i % 5][x % 107], x)
print(min_sum)
