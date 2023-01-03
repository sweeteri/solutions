"""
на производстве станок с ЧПУ обрабатывал
некоторый набор деталей. В каждый момент времени станок может обрабатывать только одну деталь.
Каждая деталь изготавливалась в определённый промежуток времени с момента начала рабочего дня.
Простоем считается временной участок длиной не менее М секунд, в которые не обрабатывается Ни одна деталь.
Инженер решил узнать, какое количество простоев произошло за день и какова длительность наибольшего простоя.
Общая длительность рабочего дня L секунд
Запишите в ответе два числа: количество простоев произошло за день и какова длительность наибольшего простоя.
"""

with open('26.txt') as f:

    l, m, n = map(int, f.readline().split())
    work = [0] * (l + 1)
    for i in f:
        start, end = map(int, i.split())
        work[start] += 1
        work[end + start] -= 1

    wasted_time_period, max_wasted_time_period, amount = 0, 0, 0
    curr = 0
    for i in range(l + 1):
        curr += work[i]
        if curr == 0:
            wasted_time_period += 1
            if i == l and wasted_time_period >= m:
                max_wasted_time_period = max(max_wasted_time_period, wasted_time_period)
                amount += 1

        else:
            if wasted_time_period >= m:
                max_wasted_time_period = max(max_wasted_time_period, wasted_time_period)
                amount += 1
            wasted_time_period = 0


print(amount, max_wasted_time_period-1)
