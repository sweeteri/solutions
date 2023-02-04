"""
Необходимо определить минимальную сумму двух элементов, кратную 23,
при этом произведение этих чисел должно делиться на 6,
а расстояние между двумя элементами не менее 7.
"""
with open('27B.txt') as f:
    n = int(f.readline())
    min_sum = 20 ** 5 + 1
    q = [int(f.readline()) for _ in range(6)]
    mods = [[20 ** 5 + 1] * 23 for _ in range(6)]
    for _ in range(n - 6):
        x = int(f.readline())
        mod = 0 if x % 23 == 0 else 23 - x % 23
        for i in range(6):  # подбираем множитель по остатку
            if x * i % 6 == 0:
                min_sum = min(min_sum, x + mods[i][mod])
        mods[q[0] % 6][q[0] % 23] = min(mods[q[0] % 6][q[0] % 23], q[0])
        q.append(x)
        q.pop(0)
print(min_sum)
