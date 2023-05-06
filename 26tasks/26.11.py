"""
В аэропорту есть камера хранения из K ячеек, которые пронумерованы с 1.
Принимаемый багаж кладется в свободную ячейку с минимальным номером.
Известно время, когда пассажиры сдают и забирают багаж (в минутах с начала суток).
Ячейка доступна для багажа, начиная со следующей минуты, после окончания срока хранения.
Если свободных ячеек не находится, то багаж не принимается в камеру хранения.
Найдите количество багажа, которое будет сдано в камеры за 24 часа и номер ячейки,
в которую сдаст багаж последний пассажир.
"""
with open('26.txt') as f:
    k = int(f.readline())
    passengers = int(f.readline())
    luggage_time = []

    for i in f:
        start, end = map(int, i.split())
        luggage_time.append([start, end])
    luggage_time.sort()

    storage = [0] * (k + 1)
    amount = 0
    last_cell = 0
    for i in luggage_time:
        for j in range(1, len(storage)):
            if i[0] >= storage[j]:
                storage[j] = i[1] + 1
                amount += 1
                last_cell = j
                break

print(amount, last_cell)