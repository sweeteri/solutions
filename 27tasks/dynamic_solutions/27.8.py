# максимальная четная сумма пары чисел, хотя бы 1 элемент, которой кратен 23
with open('27B.txt') as f:
    n = int(f.readline())
    m0, m1, m230, m231 = 0, 0, 0, 0
    for _ in range(n):
        x = int(f.readline())
        if x % 23 == 0:
            if x % 2:
                m231 = max(m231, x)
            else:
                m230 = max(m230, x)
        else:
            if x % 2:
                m1 = max(m1, x)
            else:
                m0 = max(m0, x)
print(max(m230 * 2, m231 * 2, m230 + m0, m231 + m1))
