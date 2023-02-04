# количество пар чисел, произведение, которых кратно 65
with open('27B.txt') as f:
    n = int(f.readline())
    k5, k13, k65, k = 0, 0, 0, 0
    for i in range(n):
        x = int(f.readline())
        if x % 65 == 0:
            k += i
            k65 += 1
            k13 += 1
            k5 += 1
        elif x % 5 == 0:
            k += k13
            k5 += 1
        elif x % 13 == 0:
            k += k5
            k13 += 1
        else:
            k += k65
print(k)