# количество пар сумма которых делится на 80 и хотя бы один элемент из пары больше 50000
with open('27B.txt') as f:
    n = int(f.readline())
    k = 0
    mods = [0]*80
    mods_bigger_50000 = [0]*80
    for _ in range(n):
        x = int(f.readline())
        if x > 50000:
            if x % 80 == 0:
                k += mods[0] + mods_bigger_50000[0]
                mods_bigger_50000[0] += 1
            else:
                k += mods[80 - x % 80] + mods_bigger_50000[80 - x % 80]
                mods_bigger_50000[x % 80] += 1
        else:
            if x % 80 == 0:
                k += mods_bigger_50000[0]
                mods[0] += 1
            else:
                k += mods_bigger_50000[80 - x % 80]
                mods[x % 80] += 1
print(k)
