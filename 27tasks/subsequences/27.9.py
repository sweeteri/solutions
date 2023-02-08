"""
Дана последовательность из натуральных чисел.
Рассматриваются все её непрерывные подпоследовательности длиной не менее пяти элементов,
такие что сумма элементов каждой из них кратна k = 117.
Найдите количество таких подпоследовательностей.
"""
with open('27B.txt') as f:
    n = int(f.readline())
    k = 0
    s = 0
    q = []
    mods = [0] * 117

    for _ in range(4):
        s += int(f.readline())
        q.append(s)

    for _ in range(n - 4):
        s += int(f.readline())
        if s % 117 == 0: k += 1
        k += mods[s % 117]
        mods[q[0] % 117] += 1
        q.pop(0)
        q.append(s)

print(k)