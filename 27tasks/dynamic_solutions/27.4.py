# количество пар, сумма, которых кратна 131
with open('27B.txt') as f:
    n = int(f.readline())
    mods = [0] * 131
    k = 0
    for _ in range(n):
        x = int(f.readline())
        if x % 131 == 0:
            k += mods[0]
            mods[0] += 1
        else:
            k += mods[131 - x % 131]
            mods[x % 131] += 1
print(k)
