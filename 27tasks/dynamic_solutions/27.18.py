"""
количество пар элементов этой последовательности,
сумма которых не более m=134, при этом
первый элемент пары должен быть больше второго
"""
with open('27B.txt') as f:
    n = int(f.readline())
    k = 0
    mods = [0] * 134
    for _ in range(n):
        x = int(f.readline())
        if x < 134:
            for j in range(x + 1, 134):
                if (x + j) <= 134:
                    k += mods[j]
            mods[x] += 1
print(k)
