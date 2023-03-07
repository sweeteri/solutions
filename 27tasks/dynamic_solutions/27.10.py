"""
Необходимо определить количество пар элементов,
первое число меньше второго, произведение этих чисел делится на 13,
а номера чисел в последовательности отличаются не менее, чем на 5,
сумма нечетна
"""
with open('27B.txt') as f:
    n = int(f.readline())
    q = [int(f.readline()) for _ in range(4)]
    k, k130, k131, k1, k0 = 0, 0, 0, 0, 0
    for i in range(n - 4):
        x = int(f.readline())
        if x % 13 == 0:
            k += k0 if x % 2 else k1
        else:
            k += k130 if x % 2 else k131

        if q[0] % 13 == 0:
            if q[0] % 2:
                k131 += 1
            else:
                k130 += 1
        if q[0] % 2: k1 += 1
        if q[0] % 2 == 0: k0 += 1
        q.append(x)
        q.pop(0)
print(k)
