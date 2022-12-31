with open('26.txt') as f:
    f.readline()
    d = {}
    for i in f:
        row, place = map(int, i.split())
        d.setdefault(row, set()).add(place)

k, min_row, max_trees = 0, 0, 0
for i in sorted(d):
    if len(d[i]) == 1:
        k += 1
    else:
        v = sorted(d[i])
        if len(v) == 2:
            if v[1] - v[0] in (3, 4):
                k += 1
            elif v[1] - v[0] >= 5:
                k += 2
        else:
            kk = 0

            if v[1] - v[0] > 2:
                v[0] += 2
                kk += 1

            for j in range(1, len(v) - 1):
                if v[j] - v[j - 1] <= 2 or v[j + 1] - v[j] <= 2:
                    continue
                else:
                    v[j] += 2
                    kk += 1

            if v[-1] - v[-2] > 2:
                kk += 1

            k += kk
            if kk > max_trees:
                max_trees = kk
                min_row = i

print(k, min_row)
