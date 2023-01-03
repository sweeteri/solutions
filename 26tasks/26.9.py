'''
При проведении эксперимента заряженные частицы попадают на чувствительный экран,
представляющий из себя матрицу пикселей размером 10000 на 10000 точек.
При попадании очередной частицы на экран в файл записываются координаты чувствительного элемента:
номер строки (целое число от 1 до 10000) и номер позиции в строке (целое число от 1 до 10000)
и её заряд (+/-). Положительно заряженная частица включает пиксель,
а отрицательно заряженная выключает. Положительная частица не влияет на включенный пиксель,
как и отрицательно заряженная на выключенный. Определите на момент завершения эксперимента номер строки,
в которой находится наибольшая непрерывная цепочка включенных пикселей.
'''

with open('26.txt') as f:
    f.readline()
    d = {}

    for i in f:
        k, v, flag = i.split()
        k, v = int(k), int(v)
        if flag == '+':
            d.setdefault(k, set()).add(v)

    max_counter, pos_max = 0, 0

    for i in sorted(d):
        k, v = i, d[i]
        if len(v) >= 2:
            v = sorted(v)
            max_counter_string, counter = 0, 1
            for j in range(len(v) - 1):
                if v[j + 1] - v[j] == 1:
                    counter += 1
                    max_counter_string = max(max_counter_string, counter)
                else:
                    counter = 1

            if max_counter_string >= max_counter:
                max_counter = max_counter_string
                pos_max = k


print(max_counter, pos_max)
