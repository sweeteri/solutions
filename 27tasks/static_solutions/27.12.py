# максимальная четная сумма пары чисел, в которой хотя бы один кратный 23

with open('27B.txt') as f:
    n = int(f.readline())
    k230, k231, k1, k0 = [], [], [], []
    for _ in range(n):
        x = int(f.readline())
        if x % 23 == 0:
            if x % 2:
                k231.append(x)
            else:
                k230.append(x)
        else:
            if x % 2:
                k1.append(x)
            else:
                k0.append(x)
k230.sort()
k231.sort()
print(max(k230[-1] + k230[-2], k231[-1] + k231[-2], k230[-1] + max(k0), k231[-1] + max(k1)))
