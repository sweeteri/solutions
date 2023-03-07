"""
Необходимо определить количество пар элементов,
первое число меньше второго, произведение этих чисел делится на 23,
а номера чисел в последовательности отличаются не менее, чем на 9.
"""
with open('27A.txt') as f:
    n = int(f.readline())
    k, k23 = 0, 0
    q = [int(f.readline()) for _ in range(8)]
    for i in range(n - 8):
        x = int(f.readline())
        k += i if x%23==0 else k23

        if q[0] % 23 == 0: k23 += 1

        q.pop(0)
        q.append(x)
print(k)
