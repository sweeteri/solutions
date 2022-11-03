# кол-во пар сичел, произведение которых кратно 7

with open('27B.txt') as f:
    n = int(f.readline())
    k7, k = 0, 0
    for _ in range(n):
        if int(f.readline()) % 7 == 0:
            k7 += 1
        else:
            k += 1
print(k * k7 + k7 * (k7 - 1) // 2)
