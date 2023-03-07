# количество пар чисел, произведение, которых кратно 7
with open('27B.txt') as f:
    n = int(f.readline())
    k7, k = 0, 0
    for i in range(n):
        x = int(f.readline())
        if x % 7 == 0:
            k += i
            k7 += 1
        else:
            k += k7
print(k)