"""
Дана последовательность, состоящая из N целых неотрицательных чисел.
Рассматриваются подпоследовательности исходной последовательности,
состоящие из K элементов и содержащие в себе хотя бы один нуль.
Гарантируется, что K - нечётное.
Среди этих подпоследовательностей найти такие, в которых суммы элементов,
расположенных по разные стороны от центра, равны.
Центральное число в суммы не учитывается.
Найти количество подходящих подпоследовательностей.
"""
# 70 65
with open('27B.txt') as f:
    n, k = map(int, f.readline().split())
    q, d = [], {}

    for _ in range(k):
        x = int(f.readline())
        q.append(x)
        d[x] = d.get(x, 0) + 1

    counter = 0
    for i in range(n - k):
        x = int(f.readline())
        if 0 in d and d[0] > 0:
            if sum(q[:k // 2]) == sum(q[k // 2 + 1:]):
                counter += 1

        if d[q[0]] > 0:
            d[q[0]] -= 1
        d[x] = d.get(x, 0) + 1
        q.pop(0)
        q.append(x)

print(counter)