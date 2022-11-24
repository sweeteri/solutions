'''Задача про ряды. Надо найти максимальный ряд, в котором есть 2 подряд свободных места,
причем места вокруг них должны быть заняты.
Вывод: максимальный номер такого ряда, минимальный номер такого(свободного) места.
'''

with open('26.txt') as f:
    N = int(f.readline())
    d = {}
    max_row, min_seat = 0, 0

    for i in f:
        k, v = map(int, i.split())
        d.setdefault(k, []).append(v)

    d = sorted(d.items(), key=lambda x: x[0], reverse=True)

    for i in d:
        k, v = i[0], i[1]
        if len(v) >= 2:
            v.sort()
            for j in range(len(v) - 1):
                if abs(v[j] - v[j + 1]) == 3:
                    max_row, min_seat = k, v[j]
                    break
            if max_row != 0:
                break

print(max_row, min_seat)
