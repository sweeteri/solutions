"""
Дана последовательность целых чисел.
Рассматриваются все её непрерывные подпоследовательности длиной не менее семи элементов,
такие что количество положительных чисел кратных 7 делится на 7.
Найдите наибольшую сумму такой подпоследовательности.
"""
with open('27A.txt') as f:
    n = int(f.readline())
    s, max_sum = 0, -2 * 10 ** 9 - 1
    k = 0
    q = []
    mods = [10 ** 20] * 7

    for _ in range(6):
        x = int(f.readline())
        s += x
        if x > 0 and x % 7 == 0: k += 1
        q.append([s, k])

    for _ in range(n - 6):
        x = int(f.readline())
        s += x
        if x > 0 and x % 7 == 0: k += 1
        if k % 7 == 0: max_sum = max(max_sum, s)
        max_sum = max(max_sum, s - mods[k % 7])
        mods[q[0][1] % 7] = min(mods[q[0][1] % 7], q[0][0])
        q.pop(0)
        q.append([s, k])

print(max_sum)
