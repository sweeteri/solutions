"""
определить количество пар, для которых произведение элементов заканчивается на 3,
 а номера чисел в последовательности отличаются не менее, чем на 6.
"""
with open('27B.txt') as f:
    n = int(f.readline())
    q = [int(f.readline()) for _ in range(5)]
    k1, k3, k7, k9, k = 0, 0, 0, 0, 0
    for _ in range(n - 5):
        x = int(f.readline())
        if x % 10 == 1: k += k3
        if x % 10 == 3: k += k1
        if x % 10 == 7: k += k9
        if x % 10 == 9: k += k7

        if q[0] % 10 == 1: k1 += 1
        if q[0] % 10 == 3: k3 += 1
        if q[0] % 10 == 7: k7 += 1
        if q[0] % 10 == 9: k9 += 1

        q.append(x)
        q.pop(0)
print(k)
