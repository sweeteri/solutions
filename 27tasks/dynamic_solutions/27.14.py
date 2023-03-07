"""
Необходимо определить минимальную сумму пары чисел кратную 144,
 при этом первый элемент пары должен быть меньше второго
"""
with open('27B.txt') as f:
    n = int(f.readline())
    mods = [10 ** 5 + 1] * 144
    for _ in range(n):
        x = int(f.readline())
        mods[x % 144] = min(x, mods[x % 144])

res = []
for i in range(1, 72):
    res.append(mods[i] + mods[144 - i])
print(min(res))
