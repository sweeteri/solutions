"""
Дана последовательность целых чисел.
Необходимо найти максимально возможную сумму её непрерывной подпоследовательности,
в которой количество положительных чётных элементов кратно k = 30
"""
with open('27A.txt') as f:
    n = int(f.readline())
    k = 0
    max_sum, s = -2 * 10 ** 9 - 1, 0
    mods = [2 * 10 ** 9 - 1] * 30
    for _ in range(n):
        x = int(f.readline())
        s += x
        if x > 0 and x % 2 == 0: k += 1

        if k % 30 == 0: max_sum = max(max_sum, s)

        max_sum = max(max_sum, s - mods[k % 30])
        mods[k % 30] = min(mods[k % 30], s)

print(max_sum)
