# максимальная нечетная сумма пары
with open('27A.txt') as f:
    n = int(f.readline())
    k0, k1 = 0, 0
    for _ in range(n):
        x = int(f.readline())
        if x % 2:
            k1 = max(k1, x)
        else:
            k0 = max(k0, x)
print(k0 + k1)
