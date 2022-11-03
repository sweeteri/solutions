with open('26.py.txt') as f:
    global_counter = 0
    strh = 0
    n = f.readline()
    d = {}
    for i in f:
        k, v, fl = i.split()
        k, v = int(k), int(v)
        if fl == '+':
            d.setdefault(k, []).append(v)
    d = dict(filter(lambda x: len(x[1]) > 2, d.items()))
    d = sorted(d.items(), key=lambda x: x[0])
    for i in d:
        k, v = i
        v.sort()
        counter = 0
        if len(v) == 1:
            continue
        for j in range(len(v) - 1):

            if v[j + 1] - v[j] == 1:
                counter += 1
            else:
                if counter > global_counter:
                    global_counter = counter
                    counter = 0
                    strh = k

print(global_counter, strh)
