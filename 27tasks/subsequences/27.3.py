"""
Дана последовательность натуральных чисел
Рассматриваются все её непрерывные подпоследовательности,
в которых количество чисел, делящихся на 5, кратно 11.
Найдите количество таких подпоследовательностей
"""
with open('27B.txt') as f:
    n = int(f.readline())
    mods = [0] * 11
    k5 = 0
    k = 0
    for _ in range(n):
        x = int(f.readline())
        if x % 5 == 0: k5 += 1
        if k5 % 11 == 0: k += 1
        k += mods[k5 % 11]
        mods[k5 % 11] += 1

print(k)
