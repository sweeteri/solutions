with open('27B.txt') as f:
    f.readline()
    ost = [0] * 131
    for i in f:
        x = int(i)
        ost[x % 131] += 1
k = (ost[0] * (ost[0] - 1)) // 2
for i in range(1, 66):
    k += ost[i] * ost[131 - i]
print(k)
