# максимальная нечетная сумма пары
with open('27B.txt') as f:
    n = int(f.readline())
    nc, c = [], []
    for _ in range(n):
        x = int(f.readline())
        if x % 2:
            nc.append(x)
        else:
            c.append(x)
nc.sort()
c.sort()
print(nc[-1]+c[-1])