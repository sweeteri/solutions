'''Задача про ряды. Надо найти максимальный ряд, в котором есть 2 подряд свободных места,
причем места вокруг них должны быть заняты.
Вывод: максимальный номер такого ряда, минимальный номер такого(свободного) места.
'''

with open(r'C:\Users\MAX\Pictures\26_1_2.txt') as f:
    N = int(f.readline())
    mr, mm = 0, 0
    d = {}

    for i in f:
        k, v = map(int, i.split())
        d.setdefault(k, []).append(v)

    d = sorted(d.items(), key=lambda x: x[0], reverse=True)

    for i in d:
        k, v = i[0], i[1]
        v.sort()
        if len(v) in (0, 1):
            continue
        elif len(v) == 2 and abs(v[0] - v[1]) == 3:
            mr, mm = k, v[0]
            break
        else:
            for j in range(len(v) - 1):
                if abs(v[j] - v[j + 1]) == 3:
                    mr, mm = k, v[j]
                    break
        if mr != 0:
            break

print(mr, mm)
