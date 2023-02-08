"""
Дана последовательность натуральных чисел.
Рассматриваются все её непрерывные подпоследовательности,
в которых количество чисел, делящихся на 5, кратно 3.
Найдите наибольшую сумму такой подпоследовательности.
"""
with open('27B.txt') as f:
    n = int(f.readline())
    max_sum, s = 0, 0
    k5 = 0
    mods = [20 ** 5] * 3
    for _ in range(n):
        x = int(f.readline())
        s += x
        if x % 5 == 0: k5 += 1
        if k5 % 3 == 0: max_sum = max(max_sum, s)
        max_sum = max(max_sum, s - mods[k5 % 3])
        mods[k5 % 3] = min(mods[k5 % 3], s)
print(max_sum)
