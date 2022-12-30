with open('27-A.txt') as f:
    f.readline()
    s_min, s_max = 0, 0
    min_ost = [9999] * 7
    ost = []

    for i in f:
        x, y = sorted(map(int, i.split()))
        s_min += x
        s_max += y
        diff = y - x

        if diff < min_ost[diff % 7]:
            min_ost[diff % 7] = diff
        ost.append(diff)

ost.sort()

if s_min % 7 == s_max % 7:
    print(s_max)
else:
    w = s_max % 7 - s_min % 7
    v = s_max - min_ost[w] if s_min % 7 < s_max % 7 else s_max - min_ost[7 + w]

    for i in ost:
        if s_max < v:
            print(v)
            break
        if (s_max - i) % 7 == s_min % 7:
            print(s_max - i)
            break
        else:
            s_max -= i
