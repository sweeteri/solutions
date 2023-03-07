"""
Дана последовательность натуральных чисел.
Найти последовательность подряд идущих чисел,
чтобы их сумма была максимальной и делилась на 100
"""
with open('27A.txt') as f:
    n = int(f.readline())
    s = 0
    max_sum = 0
    mods = [20 ** 5] * 1000
    for _ in range(n):
        x = int(f.readline())
        s += x
        if s % 1000 == 0:
            max_sum = max(max_sum, s)
        else:
            max_sum = max(max_sum, s - mods[s % 1000])
        mods[s % 1000] = min(mods[s % 1000], s)
print(max_sum)
