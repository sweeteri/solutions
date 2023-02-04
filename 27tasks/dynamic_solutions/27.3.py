# количество пар чисел, произведение, которых кратно 5, а сумма нечетна
with open('27B.txt') as f:
    n = int(f.readline())
    k50, k51, k1, k0, k = 0, 0, 0, 0, 0
    for i in range(n):
        x = int(f.readline())
        # count pairs
        if x % 5 == 0:
            k += k0 if x % 2 else k1
        else:
            k += k50 if x % 2 else k51
        # update counters
        if x % 5 == 0:
            if x % 2:
                k51 += 1
            else:
                k50 += 1
        if x % 2 == 0: k0 += 1
        if x % 2: k1 += 1
print(k)
