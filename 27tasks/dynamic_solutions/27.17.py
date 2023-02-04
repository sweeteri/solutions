"""
Рассматриваются все пары различных элементов последовательности,
находящихся на расстоянии не больше чем 11
(разница в индексах элементов пары должна быть 11 или менее,
порядок элементов в паре неважен).
Необходимо найти минимальную чётную сумму, кратную 1071.
"""
with open('27A.txt') as f:
    n = int(f.readline())
    arr = []
    min_sum = 20 ** 5 + 1
    for _ in range(n):
        x = int(f.readline())
        for j in arr:
            if (x + j) % 2 == 0 and (x + j) % 1071 == 0:
                min_sum = min(min_sum, x + j)
        # adding element to queue
        arr.append(x)
        if len(arr) > 11:
            arr.pop(0)
print(min_sum)
