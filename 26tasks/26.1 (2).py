with open('26.txt') as f:
    f.readline()
    d = {}

    for i in f:
        k, v, flag = i.split()
        k, v = int(k), int(v)
        if flag == '+':
            d.setdefault(k, []).append(v)

    d = sorted(d.items(), key=lambda x: x[0])

    counter, max_counter, pos_max = 0, 0, 0

    for i in d:
        k, v = i
        if len(v) >= 2:
            v.sort()
            for j in range(len(v) - 1):
                if v[j + 1] - v[j] == 1:
                    counter += 1
                else:
                    if counter > max_counter:
                        pos_max = k
                        max_counter = counter
                        counter = 0


print(max_counter, pos_max)
